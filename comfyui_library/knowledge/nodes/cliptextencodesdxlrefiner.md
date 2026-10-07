# CLIPTextEncodeSDXLRefiner

## 节点类型

`CLIPTextEncodeSDXLRefiner`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（2 次）
- `text:STRING`（2 次）

## 输出

- `CONDITIONING:CONDITIONING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[6, 1024, 1024, "\"Imagine a small, adorable feline, bathed in the vibrant, swirling colors characteristic of Vincent va`（1 次）
- `[3, 1024, 1024, "skin spots,acnes,skin blemishes,age spot,mutated hands,mutated fingers,deformed,bad anatomy,disfigured,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
