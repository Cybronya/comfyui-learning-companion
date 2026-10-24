---
name: unknown_workflow_lora_sampler_unet_162
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.79275
common_nodes: [CLIPLoader, EmptyImage, EmptyLatentImage, INTConstant, KSampler, Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ResolutionSelector, SaveImage, Text Multiline, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy seed]
problems: []
missing: []
members: [图片生成/图生图/Qwen 2.1超细节 洗图生图2合1工作流（Qwen3.5自由切换版）😼_2102236389680177153.json, 图片生成/图生图/Qwen image 2.1超细节多图像编辑工作流_2102274071047270401.json, 图片生成/文生图/Qwen 2.1超细节 洗图生图2合1工作流（哈基米自由切换版）😼_2102228639399108609.json, 视频生成/图生视频/Qwen_2.1超细节_洗图生图2合1工作流哈基米自由切换版😼_2104044641724227586.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_162

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen 2.1超细节 洗图生图2合1工作流（Qwen3.5自由切换版）😼_2102236389680177153.json、图片生成/图生图/Qwen image 2.1超细节多图像编辑工作流_2102274071047270401.json、图片生成/文生图/Qwen 2.1超细节 洗图生图2合1工作流（哈基米自由切换版）😼_2102228639399108609.json、视频生成/图生视频/Qwen_2.1超细节_洗图生图2合1工作流哈基米自由切换版😼_2104044641724227586.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptyImage`
- `EmptyLatentImage`
- `INTConstant`
- `KSampler`
- `Label (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `Switch any [Crystools]` —— 3/4 个有
- `TextGenerateLTX2Prompt` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `RH_LLMAPI_Pro_Node` —— 2/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `QwenImage21Cache` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有
- `llama_cpp_parameters` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 25 | 25 - 25 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
