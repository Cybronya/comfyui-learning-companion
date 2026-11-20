---
name: image_to_image_lora_sampler_clip_59
type: Image To Image
frequency: 6
level: moderate
coverage: 0.842333
common_nodes: [CLIPTextEncode, DualCLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Kontext 换脸【百分比换脸】_1939599546001367041.json, 平台全量/kontext开源老照片修复（效果炸裂）提示词很关键_1939277847368278017.json, 平台全量/纠正背景透视（产品）_1974772300581089281.json, 平台全量/老照片一键修复工作流-LORA加强版V2_1947299841471844354.json, 平台全量/老照片修复工作流-LORA加强版V2_1944362292316393473.json, 平台全量/老照片修复工作流-LORA加强版_1943601295863259137.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_59

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Kontext 换脸【百分比换脸】_1939599546001367041.json、平台全量/kontext开源老照片修复（效果炸裂）提示词很关键_1939277847368278017.json、平台全量/纠正背景透视（产品）_1974772300581089281.json、平台全量/老照片一键修复工作流-LORA加强版V2_1947299841471844354.json、平台全量/老照片修复工作流-LORA加强版V2_1944362292316393473.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 5/6 个有
- `ConditioningZeroOut` —— 5/6 个有
- `FluxGuidance` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `UNETLoader` —— 5/6 个有
- `Anything Everywhere` —— 3/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `ChinesePrompt_Mix` —— 2/6 个有
- `ImageResize+` —— 2/6 个有
- `LBMSampler` —— 1/6 个有
- `LoadLBMModel` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有
- `easy imageDetailTransfer` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 6 | 56% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 0.98 | 0.91 - 1 | 6 | 97% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 0.98，观测区间 0.91 - 1，6 个样本，取值集中（一致性 97%）
