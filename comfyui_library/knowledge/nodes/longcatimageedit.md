# LongCatImageEdit

## 节点类型

`LongCatImageEdit`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `longcat_pipeline:LONGCAT_PIPE`（5 次）
- `image:IMAGE`（5 次）
- `prompt:STRING`（5 次）
- `negative_prompt:STRING`（5 次）
- `steps:INT`（5 次）
- `guidance_scale:FLOAT`（5 次）
- `seed:INT`（5 次）

## 输出

- `IMAGE:IMAGE`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["镜头向右旋转", "", 50, 4.5, 254490090324973, "randomize"]`（1 次）
- `["Turn the object in red frames into a pirate ship,remove red frames", "", 50, 4.5, 597330321244084, "randomize"]`（1 次）
- `["Remove the laptop, add a mug, change the wall to yellow, add a girl sitting on the bed, turn on the TV", "", 50, 4.5, `（1 次）
- `["", "", 50, 4.5, 488390125959888, "randomize"]`（1 次）
- `["给她戴个墨镜", "", 50, 4.5, 76924220711548, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
