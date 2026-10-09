# FaceParsingResultsParser(FaceParsing)

## 节点类型

`FaceParsingResultsParser(FaceParsing)`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `result:FACE_PARSING_RESULT`（1 次）
- `background:BOOLEAN`（1 次）
- `skin:BOOLEAN`（1 次）
- `nose:BOOLEAN`（1 次）
- `eye_g:BOOLEAN`（1 次）
- `r_eye:BOOLEAN`（1 次）
- `l_eye:BOOLEAN`（1 次）
- `r_brow:BOOLEAN`（1 次）
- `l_brow:BOOLEAN`（1 次）
- `r_ear:BOOLEAN`（1 次）

## 输出

- `MASK:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, true, true, true, true, true, true, true, false, false, true, true, true, false, false, false, false, false, fal`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
