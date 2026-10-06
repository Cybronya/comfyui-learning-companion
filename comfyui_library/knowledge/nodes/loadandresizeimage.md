# LoadAndResizeImage

## 节点类型

`LoadAndResizeImage`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:COMBO`（11 次）
- `resize:BOOLEAN`（11 次）
- `width:INT`（11 次）
- `height:INT`（11 次）
- `repeat:INT`（11 次）
- `keep_proportion:BOOLEAN`（11 次）
- `divisible_by:INT`（11 次）
- `mask_channel:COMBO`（11 次）
- `background_color:STRING`（11 次）
- `upload:IMAGEUPLOAD`（11 次）

## 输出

- `image:IMAGE`（11 次）
- `mask:MASK`（11 次）
- `width:INT`（11 次）
- `height:INT`（11 次）
- `image_path:STRING`（11 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["PQ5.png", true, 1024, 1024, 1, true, 32, "alpha", "", "image"]`（7 次）
- `["ComfyUI_00002_.png", true, 1024, 1024, 1, true, 32, "alpha", "", "image"]`（1 次）
- `["260919181619_00001.png", true, 1024, 1024, 1, true, 32, "alpha", "", "image"]`（1 次）
- `["bd1649df701da9b14f06ec9e77a15772376b9728769b409a709c164b326e515d.jpg", true, 1024, 1024, 1, true, 32, "alpha", "", "im`（1 次）
- `["6e1a97524db4ab5bbb3c3ce63e94cfca0cde2cc95b561bbf6cee834640c85ce4.png", true, 1024, 1024, 1, true, 32, "alpha", "", "im`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
