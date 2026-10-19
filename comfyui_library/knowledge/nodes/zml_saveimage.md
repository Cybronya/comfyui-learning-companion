# ZML_SaveImage

## 节点类型

`ZML_SaveImage`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `图像:IMAGE`（2 次）
- `操作模式:COMBO`（2 次）
- `保存路径:STRING`（2 次）
- `文本块存储:STRING`（2 次）
- `文件名前缀:STRING`（2 次）
- `文件名后缀:STRING`（2 次）
- `使用时间戳:BOOLEAN`（2 次）
- `使用计数器:BOOLEAN`（2 次）
- `生成预览:COMBO`（2 次）
- `保存同名txt文件:COMBO`（2 次）

## 输出

- `图像:IMAGE`（2 次）
- `Help:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["保存图像", "output/sdj", "", "", "", true, false, "启用", "禁用", "禁用", 1024, "禁用"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
