---
name: image_to_image_inpaint_sampler_vae
type: Image To Image
frequency: 5
level: weak
coverage: 0.8416
common_nodes: [CLIPLoader, ConditioningZeroOut, FastCanvas, FastCanvasTool, ImageScaleToTotalPixels, InpaintCrop, InpaintStitch, KSampler, LayerUtility: CropByMask V3, LoadImage, MaskPreview+, PreviewImage, RepeatLatentBatch, SaveImage, VAEDecode, VAEEncode, VAELoader, easy ifElse, easy isMaskEmpty]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit2509万物迁移(精准还原完美产品细节)_1976931318057586690.json, 图片生成/图生图/Qwen千问万物迁移终极版_1961988552659767297.json, 图片生成/图生图/万物迁移 千问出图 3.0 【 万金油版 】_1980488439906877442.json, 图片生成/图生图/千问edit产品替换到固定的场景里_1985358602976305154.json, 图片生成/图生图/千问万物迁移溶图工作流_2054483282682761217.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_sampler_vae

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit2509万物迁移(精准还原完美产品细节)_1976931318057586690.json、图片生成/图生图/Qwen千问万物迁移终极版_1961988552659767297.json、图片生成/图生图/万物迁移 千问出图 3.0 【 万金油版 】_1980488439906877442.json、图片生成/图生图/千问edit产品替换到固定的场景里_1985358602976305154.json、图片生成/图生图/千问万物迁移溶图工作流_2054483282682761217.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `FastCanvas`
- `FastCanvasTool`
- `ImageScaleToTotalPixels`
- `InpaintCrop`
- `InpaintStitch`
- `KSampler`
- `LayerUtility: CropByMask V3`
- `LoadImage`
- `MaskPreview+`
- `PreviewImage`
- `RepeatLatentBatch`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`
- `easy isMaskEmpty`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `RBGImageStitchPlus` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `easy imageRemBg` —— 4/5 个有
- `TextEncodeQwenImageEditPlus` —— 3/5 个有
- `JjkText` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `TextEncodeQwenImageEdit` —— 2/5 个有
- `Primitive integer [Crystools]` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `RMBG` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `Text Concatenate` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 1 - 8 | 5 | 58% |
| Prompt 约束强度(CFG) | 1 | 0 - 1 | 5 | 50% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0 - 1 | 5 | 50% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 1 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 0 - 1，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0 - 1，5 个样本
- 风险：Prompt 约束强度(CFG) 观测到 0，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 风险：重绘幅度 观测到 0，低于常用下限 0.1（）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
