# Qwen3VL_Advanced

## 节点类型

`Qwen3VL_Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `🖼️ 图像1:IMAGE`（3 次）
- `🖼️ 图像2:IMAGE`（3 次）
- `🖼️ 图像3:IMAGE`（3 次）
- `🖼️ 图像4:IMAGE`（3 次）
- `🎥 视频:IMAGE`（3 次）
- `🎯 Qwen3VL额外选项:QWEN3VL_EXTRA_OPTIONS`（3 次）
- `🤖 模型选择:COMBO`（3 次）
- `⚙️ 量化级别:COMBO`（3 次）
- `🧠 注意力模式:COMBO`（3 次）
- `🖼️ 最大长边:INT`（3 次）

## 输出

- `文本输出:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen3-VL-4B-Instruct", "None (FP16)", "SDPA", 768, "提示词风格 - 详细", "请详细描述图片中人物的姿势，严禁描述人物所在的场景、服装、发型等内容，仅描述人物姿势。\n例：\n人物坐`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
