public class euclids_stuff_java_style{
public static int gcd(int num1, int num2){
    num1=Math.abs(num1);
    num2=Math.abs(num2);
    if (num1>=num2){
        int rem=num1%num2;
        if (rem==0){
            return num2;
        }
        else{
            return gcd(num2,rem);
        }}
    else{
        return gcd(num2, num1);
    }

    }
    public static void main(String[] args) {
        int result=gcd(120, 135);
        System.out.println("The GCD of the two numbers is "+result);
    }
}