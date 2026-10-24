---
name: unknown_workflow_video_sampler_clip_125
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.7348
common_nodes: [CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), INTConstant, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, Qwen3_VQA, RIFE VFI, VAEDecode, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 DaSiWa8.1 最强动漫模型视频流-单图版+补帧_2008070467520827394.json, 视频生成/图生视频/Wan2.2 DaSiWa8.1 最强动漫模型视频流-双图版+补帧_2008456378490298370.json, 视频生成/图生视频/[发布版]DaSiWa-WAN2.2场景首尾帧生视频_2033880906871611394.json, 视频生成/图生视频/[发布版]aSiWa-WAN2.2景物类单图生视频带推理_2033525595593773057.json, 视频生成/图生视频/zfl图生视频流-支持单图 _ 双图 _ 出视频 5.0_2031581531424165889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_125

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 DaSiWa8.1 最强动漫模型视频流-单图版+补帧_2008070467520827394.json、视频生成/图生视频/Wan2.2 DaSiWa8.1 最强动漫模型视频流-双图版+补帧_2008456378490298370.json、视频生成/图生视频/[发布版]DaSiWa-WAN2.2场景首尾帧生视频_2033880906871611394.json、视频生成/图生视频/[发布版]aSiWa-WAN2.2景物类单图生视频带推理_2033525595593773057.json、视频生成/图生视频/zfl图生视频流-支持单图 _ 双图 _ 出视频 5.0_2031581531424165889.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `Qwen3_VQA`
- `RIFE VFI`
- `VAEDecode`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetImagesFromBatchIndexed` —— 4/5 个有
- `JoinStrings` —— 4/5 个有
- `PainterI2V` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `SimpleMath+` —— 3/5 个有
- `TextInput_` —— 3/5 个有
- `UNETLoader` —— 3/5 个有
- `VAELoader` —— 3/5 个有
- `WanFirstLastFrameToVideo` —— 3/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `JjkText` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `RHHiddenNodes` —— 2/5 个有
- `easy convertAnything` —— 2/5 个有
- `CR Integer To String` —— 1/5 个有
- `CR Text Replace` —— 1/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `ImageLoader` —— 1/5 个有
- `MultiplePathsInput` —— 1/5 个有
- `Switch string [Crystools]` —— 1/5 个有
- `ZML_BooleanSwitch` —— 1/5 个有
- `ttN concat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 20 | 5 | 11% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 60% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 20，5 个样本，取值分散，一致性仅 11%
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 60%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
