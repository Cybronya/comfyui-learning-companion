---
name: text_to_image_lora_sampler_clip_206
type: Text To Image
frequency: 9
level: weak
coverage: 0.816444
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningKrea2Rebalance, ConditioningZeroOut, EmptyLatentImage, KSampler, Krea2ControlApply, Krea2ControlImageEncode, Krea2ControlLoRALoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, Qwen3_VQA, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea 2 深度控制_2076137156187348993.json, 图片生成/图生图/Krea2 深度控制+人物一致 高清放大 双重调节细节加强文生图2K_2082654426698969090.json, 图片生成/图生图/Krea2洗图高清放大工作流_2079105435461836801.json, 图片生成/图生图/Krea2洗图高清放大工作流_2089692430135283713.json, 图片生成/图生图/Krea2深度控制板_2075121684088180738.json, 图片生成/图生图/（贞贞版-搭建方式2）Krea2深度控制+双重调节细节加强文生图2K版_2074737002473418754.json, 图片生成/文生图/Krea2深度控制+双重调节细节加强文生图2K版V2_2074865088221237249.json, 图片生成/文生图/Krea2深度控制人物+节点51和70自定义人物lora+全节点注释_2082965427004723202.json, 图片生成/文生图/（贞贞版）Krea2深度控制+双重调节细节加强文生图2K版V2_2074766270821654529.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_206

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Krea 2 深度控制_2076137156187348993.json、图片生成/图生图/Krea2 深度控制+人物一致 高清放大 双重调节细节加强文生图2K_2082654426698969090.json、图片生成/图生图/Krea2洗图高清放大工作流_2079105435461836801.json、图片生成/图生图/Krea2洗图高清放大工作流_2089692430135283713.json、图片生成/图生图/Krea2深度控制板_2075121684088180738.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningKrea2Rebalance`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `Krea2ControlApply`
- `Krea2ControlImageEncode`
- `Krea2ControlLoRALoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LatentUpscaleBy` —— 8/9 个有
- `CR Prompt Text` —— 7/9 个有
- `ImageConcanate` —— 7/9 个有
- `TextConcat` —— 7/9 个有
- `DuckHideNode` —— 4/9 个有
- `Float` —— 4/9 个有
- `AddLabel` —— 2/9 个有
- `GetNode` —— 2/9 个有
- `SetNode` —— 2/9 个有
- `easy float` —— 2/9 个有
- `easy getNode` —— 2/9 个有
- `easy setNode` —— 2/9 个有
- `CR Text` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `PDIMAGE_LongerSize` —— 1/9 个有
- `solarL_SaveImagesToZip` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 9 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 9 | 21% |
| 采样算法 | euler_ancestral | - | 9 | 44% |
| 调度器 | sgm_uniform | - | 9 | 44% |
| 重绘幅度 | 1 | 0.3 - 1 | 9 | 52% |
| 宽度 | 1024 | 80 - 1024 | 9 | 68% |
| 高度 | 1536 | 80 - 1536 | 9 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，9 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，9 个样本，取值分散，一致性仅 21%
- 采样算法 最常用 euler_ancestral，9 个样本，一致性 44%
- 调度器 最常用 sgm_uniform，9 个样本，一致性 44%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，9 个样本
- 宽度 中位数 1024，观测区间 80 - 1024，9 个样本
- 高度 中位数 1536，观测区间 80 - 1536，9 个样本
- 高发问题（17/9 个样本）：Steps较低可能导致细节不足
