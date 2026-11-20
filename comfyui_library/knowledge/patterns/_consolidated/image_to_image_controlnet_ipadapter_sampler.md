---
name: image_to_image_controlnet_ipadapter_sampler
type: Image To Image
frequency: 21
level: moderate
coverage: 0.91119
common_nodes: [AIO_Preprocessor, BrushNet, BrushNetLoader, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ConditioningZeroOut, Control Net Stacker, ControlNetLoader, DeepTranslatorTextNode, Efficient Loader, IPAdapterAdvanced, KSampler, KSampler (Efficient), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一句话变魔鬼_1935242145739767809.json, 图片生成/图生图/一句话换老虎头_1935225745645948929.json, 图片生成/图生图/幻想3D立体风景加速版_1935939510553206785.json, 图片生成/图生图/涂鸦变炫彩动漫_1935611627654021121.json, 图片生成/图生图/真人转动漫+深度推算_1936329375300358146.json, 图片生成/图生图/真人转动漫+线稿_1938118211391131649.json, 图片生成/图生图/真人转动漫CN控制_1937773355569451010.json, 图片生成/图生图/真人转动漫双姿态控制_1936313303201386498.json, 图片生成/图生图/真人转动漫姿态+模糊线控制_1935618797447335937.json, 图片生成/图生图/真人转动漫姿态+法向控制_1936319081991557121.json, 图片生成/图生图/真人转动漫姿态+深度控制_1936316321263161346.json, 图片生成/图生图/真人转动漫姿态控制_1935953318810148865.json, 图片生成/图生图/真人转绘动漫加速版_1935619530326462466.json, 图片生成/图生图/真人转绘动漫画风加速版_1935943328997236738.json, 图片生成/图生图/真人转迪士尼皮克斯3D动画+线稿_1938121889954840578.json, 图片生成/图生图/简笔画变卡通风格_1935251247052017666.json, 图片生成/图生图/线稿上色加速版_1935948962375327745.json, 图片生成/图生图/长安荔枝来真人转动漫_1936331247067238402.json, 图片生成/图生图/长安荔枝来转动漫CN控制_1936292349280440321.json, 图片生成/图生图/雕塑混合+姿态控制_1936322273148063745.json, 图片生成/文生图/涂鸦变卡通风格_1935605881163939842.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_sampler

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/一句话变魔鬼_1935242145739767809.json、图片生成/图生图/一句话换老虎头_1935225745645948929.json、图片生成/图生图/幻想3D立体风景加速版_1935939510553206785.json、图片生成/图生图/涂鸦变炫彩动漫_1935611627654021121.json、图片生成/图生图/真人转动漫+深度推算_1936329375300358146.json…）

- **类型**：Image To Image
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 21 个 workflow 都包含：
- `AIO_Preprocessor`
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `Control Net Stacker`
- `ControlNetLoader`
- `DeepTranslatorTextNode`
- `Efficient Loader`
- `IPAdapterAdvanced`
- `KSampler`
- `KSampler (Efficient)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `BlendInpaint` —— 20/21 个有
- `SetLatentNoiseMask` —— 20/21 个有
- `GroundingDinoModelLoader (segment anything)` —— 19/21 个有
- `GroundingDinoSAMSegment (segment anything)` —— 19/21 个有
- `LoraLoaderModelOnly` —— 19/21 个有
- `SAMModelLoader (segment anything)` —— 19/21 个有
- `IPAdapterModelLoader` —— 18/21 个有
- `ControlNetApplyAdvanced` —— 17/21 个有
- `WD14Tagger|pysssss` —— 16/21 个有
- `ImageInvert` —— 5/21 个有
- `IPAdapterUnifiedLoader` —— 3/21 个有
- `MarigoldDepthEstimation` —— 3/21 个有
- `RemapDepth` —— 3/21 个有
- `easy loraStack` —— 3/21 个有
- `ColorizeDepthmap` —— 2/21 个有
- `ImageConcanate` —— 2/21 个有
- `InpaintPreprocessor` —— 1/21 个有
- `PainterNode` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 25 | 21 | 59% |
| Prompt 约束强度(CFG) | 7 | 1.5 - 8 | 21 | 49% |
| 采样算法 | dpmpp_2m | - | 21 | 57% |
| 调度器 | karras | - | 21 | 90% |
| 重绘幅度 | 1 | 0.5 - 1 | 21 | 89% |
| ControlNet 权重 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 25，21 个样本
- Prompt 约束强度(CFG) 中位数 7，观测区间 1.5 - 8，21 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 dpmpp_2m，21 个样本，一致性 57%
- 调度器 最常用 karras，21 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，21 个样本，取值集中（一致性 89%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（11/21 个样本）：Steps较低可能导致细节不足
