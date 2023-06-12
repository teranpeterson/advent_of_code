package main

import "fmt"

type monkey struct {
	count   int
	items   []int
	op      func(int) int
	divisor int
	monk_t  *monkey
	monk_f  *monkey
}

func main() {
	monkey0 := monkey{
		items:   []int{79, 98},
		op:      func(old int) int { return old * 19 },
		divisor: 23,
	}
	monkey1 := monkey{
		items:   []int{54, 65, 75, 74},
		op:      func(old int) int { return old + 6 },
		divisor: 19,
	}
	monkey2 := monkey{
		items:   []int{79, 60, 97},
		op:      func(old int) int { return old * old },
		divisor: 13,
	}
	monkey3 := monkey{
		items:   []int{74},
		op:      func(old int) int { return old + 3 },
		divisor: 17,
	}
	monkey0.monk_t = &monkey2
	monkey0.monk_f = &monkey3
	monkey1.monk_t = &monkey2
	monkey1.monk_f = &monkey0
	monkey2.monk_t = &monkey1
	monkey2.monk_f = &monkey3
	monkey3.monk_t = &monkey0
	monkey3.monk_f = &monkey1

	monkeys := []*monkey{&monkey0, &monkey1, &monkey2, &monkey3}

	for i := 0; i < 20; i++ {
		for _, mon := range monkeys {
			for _, item := range mon.items {
				mon.count++
				new := mon.op(item) / 3
				if new%mon.divisor == 0 {
					mon.monk_t.items = append(mon.monk_t.items, new)
				} else {
					mon.monk_f.items = append(mon.monk_f.items, new)
				}
			}
			mon.items = []int{}
		}
	}

	fmt.Println(monkey0.count)
	fmt.Println(monkey1.count)
	fmt.Println(monkey2.count)
	fmt.Println(monkey3.count)

}
