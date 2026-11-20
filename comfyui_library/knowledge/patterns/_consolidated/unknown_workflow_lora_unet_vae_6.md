---
name: unknown_workflow_lora_unet_vae_6
type: Unknown Workflow
frequency: 10
level: weak
coverage: 0.8882
common_nodes: [CLIPLoader, Image Comparer (rgthree), LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit-2511简单工作流_2004484543145017346.json, 图片生成/图生图/Qwen-edit-2511 画风迁移_2076508022507139073.json, 图片生成/图生图/Qwen-快速换脸-SZ_2110932927445037058.json, 图片生成/图生图/Qwen2511 五图编辑工作流_2087794231141298177.json, 图片生成/图生图/Qwen2511 双图OOTD每日穿搭_2087795213162078209.json, 图片生成/图生图/Qwen2511产品精准溶图打光工作流_2087792356438401026.json, 图片生成/图生图/Qwen2511产品精准溶图打光工作流_2088634640620933121.json, 图片生成/图生图/Qwen2511风格迁移工作流_2087790893486141442.json, 图片生成/图生图/Qwen换脸工作流（无需遮罩）_2088161494591696898.json, 平台全量/Qwen-edit_电商超级溶图工作流_1980507881579696130.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_6

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit-2511简单工作流_2004484543145017346.json、图片生成/图生图/Qwen-edit-2511 画风迁移_2076508022507139073.json、图片生成/图生图/Qwen-快速换脸-SZ_2110932927445037058.json、图片生成/图生图/Qwen2511 五图编辑工作流_2087794231141298177.json、图片生成/图生图/Qwen2511 双图OOTD每日穿搭_2087795213162078209.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/10 个有
- `QwenImageIntegratedKSampler` —— 9/10 个有
- `PreviewImage` —— 4/10 个有
- `FastCanvas` —— 3/10 个有
- `FastCanvasTool` —— 3/10 个有
- `LayerMask: BiRefNetUltraV2` —— 3/10 个有
- `LayerMask: LoadBiRefNetModelV2` —— 3/10 个有
- `ConditioningZeroOut` —— 1/10 个有
- `GetImageSize+` —— 1/10 个有
- `ImageResize+` —— 1/10 个有
- `KSampler` —— 1/10 个有
- `LayerStyle: Stroke` —— 1/10 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/10 个有
- `VAEDecode` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 图生图 image-to-image | - | 10 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | 0 | 0 - 1472 | 9 | 0% |
| 调度器 | 0 | 0 - 1104 | 9 | 0% |
| 重绘幅度 | 999 | 1 - 8.31118e+14 | 10 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 图生图 image-to-image，10 个样本，一致性 90%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 中位数 0，观测区间 0 - 1472，9 个样本，取值分散，一致性仅 0%
- 调度器 中位数 0，观测区间 0 - 1104，9 个样本，取值分散，一致性仅 0%
- 重绘幅度 中位数 999，观测区间 1 - 8.31118e+14，10 个样本，取值分散，一致性仅 0%
- 风险：重绘幅度 观测到 8.31118e+14，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
