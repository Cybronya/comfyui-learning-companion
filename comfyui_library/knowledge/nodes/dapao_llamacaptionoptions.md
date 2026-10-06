# Dapao_LlamaCaptionOptions

## 节点类型

`Dapao_LlamaCaptionOptions`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `👤 包含人物信息:BOOLEAN`（3 次）
- `🚫 排除不可改变特征:BOOLEAN`（3 次）
- `💡 包含光照信息:BOOLEAN`（3 次）
- `📐 包含相机角度:BOOLEAN`（3 次）
- `📷 包含相机详情:BOOLEAN`（3 次）
- `💡 提及光源:BOOLEAN`（3 次）
- `🎨 包含艺术质量:BOOLEAN`（3 次）
- `📊 包含构图信息:BOOLEAN`（3 次）
- `🌈 包含景深信息:BOOLEAN`（3 次）
- `🔍 排除性感内容:BOOLEAN`（3 次）

## 输出

- `🍭llama反推选项:LLAMA_CAPTION_OPTIONS`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, false, true, true, false, true, false, true, true, false, false, false, false, false, false, false, false]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
