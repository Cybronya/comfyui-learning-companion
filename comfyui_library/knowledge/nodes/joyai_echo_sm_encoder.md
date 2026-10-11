# JoyAI_Echo_SM_Encoder

## 节点类型

`JoyAI_Echo_SM_Encoder`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 9 个 workflow 中。

## 输入

- `clip:CLIP`（9 次）
- `prefetch_count:INT`（9 次）
- `enable_streaming:BOOLEAN`（9 次）
- `prompt:STRING`（9 次）
- `prompt_files:STRING`（9 次）

## 输出

- `te_cond:CONDITIONING`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, "ID_A is Ethan Cole, a late-twenties American lifestyle vlogger with wavy brown hair, light stubble, tired blue eyes`（4 次）
- `[1, "ID_A is Ethan Cole, a late-twenties American lifestyle vlogger with wavy brown hair, light stubble, tired blue eyes`（2 次）
- `[1, "ID_A is Ethan Cole, a late-twenties American lifestyle vlogger with wavy brown hair, light stubble, tired blue eyes`（1 次）
- `[1, true, "", ""]`（1 次）
- `[1, true, "{\n  \"prompts\": [\n    \"ID_A is Ethan Cole, a late-twenties American lifestyle vlogger with wavy brown hai`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
