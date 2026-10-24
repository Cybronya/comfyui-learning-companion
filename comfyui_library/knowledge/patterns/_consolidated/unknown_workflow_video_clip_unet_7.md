---
name: unknown_workflow_video_clip_unet_7
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.834
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DF_Integer, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, ShowText|pysssss, SimpleMath+, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy int]
problems: []
missing: []
members: [视频生成/图生视频/0902FusionX - 图生视频 (加速版) + 提示词自动润色扩写_1962917195766534146.json, 视频生成/图生视频/FusionX - 图生视频 (加速版) + 提示词自动润色扩写_1947906142839144449.json, 视频生成/图生视频/FusionX - 图生视频 (加速版) + 提示词自动润色扩写_1951893131908337665.json, 视频生成/图生视频/wan2.2 图生视频 (加速版) + 自动提示词 + 润色扩写_1950000678817193986.json, 视频生成/图生视频/wan2.2 图生视频 (加速版) + 自动提示词 + 润色扩写_1952550373196279809.json, 视频生成/图生视频/wan2.2 图生视频 (加速版) + 自动提示词 + 润色扩写_1955912708610772993.json, 视频生成/图生视频/wan2.2 图生视频【加速版】+ prompt 扩写_1950367167160213505.json, 视频生成/图生视频/【wan2.2】简单高清+ 图生视频_1952551449228185602.json, 视频生成/图生视频/图生视频FusionX 版最强人物一致性（加速）_1975460851899568129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_7

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/0902FusionX - 图生视频 (加速版) + 提示词自动润色扩写_1962917195766534146.json、视频生成/图生视频/FusionX - 图生视频 (加速版) + 提示词自动润色扩写_1947906142839144449.json、视频生成/图生视频/FusionX - 图生视频 (加速版) + 提示词自动润色扩写_1951893131908337665.json、视频生成/图生视频/wan2.2 图生视频 (加速版) + 自动提示词 + 润色扩写_1950000678817193986.json、视频生成/图生视频/wan2.2 图生视频 (加速版) + 自动提示词 + 润色扩写_1952550373196279809.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DF_Integer`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ShowText|pysssss`
- `SimpleMath+`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 8/9 个有
- `RH_LLMAPI_NODE` —— 8/9 个有
- `RH_Translator` —— 8/9 个有
- `easy ifElse` —— 8/9 个有
- `string_util_StrReplace` —— 8/9 个有
- `KSamplerAdvanced` —— 5/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `INTConstant` —— 4/9 个有
- `KSampler` —— 4/9 个有
- `LayerUtility: PurgeVRAM` —— 4/9 个有
- `PatchModelPatcherOrder` —— 4/9 个有
- `RH_Captioner` —— 4/9 个有
- `TorchCompileModelWanVideoV2` —— 4/9 个有
- `MathExpression|pysssss` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 9 | 44% |
| Prompt 约束强度(CFG) | 10 | 1 - 10 | 9 | 25% |
| 采样算法 | 3.5 | 3.5 - 3.5 | 5 | 100% |
| 调度器 | euler | - | 9 | 56% |
| 重绘幅度 | simple | - | 9 | 56% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 10，9 个样本，一致性 44%
- Prompt 约束强度(CFG) 中位数 10，观测区间 1 - 10，9 个样本，取值分散，一致性仅 25%
- 采样算法 中位数 3.5，观测区间 3.5 - 3.5，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，9 个样本，一致性 56%
- 重绘幅度 最常用 simple，9 个样本，一致性 56%
