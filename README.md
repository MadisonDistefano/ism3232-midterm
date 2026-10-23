# ism3232-midterm: LongHorn Order Report

Madison Distefano
**Class:** ISM 3232, Business Application Development

This is my midterm project for ISM 3232. It uses made-up orders and sample menu
prices, so it is not a real LongHorn Steakhouse system.

## What the Program Does

My program looks at a list of five food orders. For each order it figures out
the discount, the small order fee if there is one, and the sales tax. Then it
shows one line with the order number, the guest, and the final total. At the
end it shows six summary lines: how many orders there were, the total money
made, the average order, the largest order, how many orders were big, and how
many orders got a discount.

## Business Rules

1. **Subtotal:** the plate price times the number of plates.
2. **Discount:** fewer than 5 plates get no discount. 5 to 9 plates get 15% off.
   10 or more plates get 20% off, but only if it is a birthday party. A group of
   10 or more that is not a birthday party gets 15% off.
3. **Small order fee:** if the cost after the discount is under $40.00, a $5.00
   fee is added.
4. **Order total:** the discounted cost plus the fee, plus 7.5% sales tax on
   that amount (6% Florida plus 1.5% Hillsborough County). Everything is rounded
   to the nearest cent.
5. **Big order:** any order with a total of $100.00 or more