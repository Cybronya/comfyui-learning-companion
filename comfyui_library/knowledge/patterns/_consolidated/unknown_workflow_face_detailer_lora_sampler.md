---
name: unknown_workflow_face_detailer_lora_sampler
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.868286
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyLatentImage, FaceDetailer, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, PurgeVRAM_UTK, RMBG, RTXVideoSuperResolution, ResolutionSelector, SAMLoader, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, UltralyticsDetectorProvider, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/krea2_参考图像洗图生成_2104464339951509506.json, 图片生成/图生图/krea2_clone_any_image_2073437187974189058.json, 图片生成/图生图/krea2_edit_image_2073784712790892546.json, 图片生成/图生图/krea2_reference_img_2073786882131054594.json, 图片生成/图生图/krea2_参考图像洗图生成_2104724046159106050.json, 图片生成/图生图/krea2_图片反推生图洗图_2074791529075527682.json, 数字人/数字人/krea2_参考图像洗图生成_2104381255394611201.json]
source: knowledge_consolidation
---

# unknown_workflow_face_detailer_lora_sampler

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/krea2_参考图像洗图生成_2104464339951509506.json、图片生成/图生图/krea2_clone_any_image_2073437187974189058.json、图片生成/图生图/krea2_edit_image_2073784712790892546.json、图片生成/图生图/krea2_reference_img_2073786882131054594.json、图片生成/图生图/krea2_参考图像洗图生成_2104724046159106050.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FaceDetailer`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `PurgeVRAM_UTK`
- `RMBG`
- `RTXVideoSuperResolution`
- `ResolutionSelector`
- `SAMLoader`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 2048 | 2048 - 2048 | 7 | 100% |
| 高度 | 2048 | 2048 - 2048 | 7 | 100% |
| 采样步数 | 2 | 2 - 2 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | deis | - | 7 | 100% |
| 调度器 | bong_tangent | - | 7 | 100% |
| 重绘幅度 | 0.2 | 0.2 - 0.2 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 2048，观测区间 2048 - 2048，7 个样本，取值集中（一致性 100%）
- 高度 中位数 2048，观测区间 2048 - 2048，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 2，观测区间 2 - 2，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，7 个样本，一致性 100%
- 调度器 最常用 bong_tangent，7 个样本，一致性 100%
- 重绘幅度 中位数 0.2，观测区间 0.2 - 0.2，7 个样本，取值集中（一致性 100%）
- 高发问题（14/7 个样本）：Steps较低可能导致细节不足
