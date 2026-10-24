---
name: image_to_image_upscale_lora_sampler_4
type: Image To Image
frequency: 20
level: moderate
coverage: 0.8634
common_nodes: [CFGNorm, CLIPLoader, Image Comparer (rgthree), ImageScaleBy, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ywt换姿势_2059923007493206018.json, 图片生成/图生图/人物姿势参考图_2061617694088192001.json, 图片生成/图生图/全自动换装+指定人脸 动作迁移_2070478132422987777.json, 图片生成/图生图/全自动换装+指定人脸 动作迁移美图生成-超高一致性+高清输出+姿势可控+多图编辑+姿势参考-高清放大_2060190864319799298.json, 图片生成/图生图/动作模仿全新调整版  人物姿势  姿势生成  姿势迁移  动作迁移_2078762792903077889.json, 图片生成/图生图/动作迁移-超高一致性 高清放大_2084839325207973890.json, 图片生成/图生图/动作迁移-超高一致性 高清输出 姿势可控 多图编辑 全自动换装 指定人脸-姿势参考-高清放大_2059071035131125762.json, 图片生成/图生图/动作迁移-超高一致性(高清输出）_1991568706801188866.json, 图片生成/图生图/姿势参考  人物姿势  姿势生成  姿势迁移  动作迁移_2067118401599918082.json, 图片生成/图生图/姿势参考  人物姿势  姿势生成  姿势迁移  动作迁移_2067163777568690178.json, 图片生成/图生图/姿势参考  人物姿势  姿势生成  姿势迁移  动作迁移_2067177565739110401.json, 图片生成/图生图/姿势参考  人物姿势  姿势生成  姿势迁移  动作迁移_2067181809313607681.json, 图片生成/图生图/姿势参考  人物姿势  姿势生成  姿势迁移  动作迁移_2067198098614603778.json, 图片生成/图生图/姿势参考  人物姿势  姿势生成  姿势迁移  动作迁移_2067266054715432961.json, 图片生成/图生图/姿势迁移 动作模仿 人物姿势++姿势生成 动作迁移 全新调整版_2079092595036344321.json, 图片生成/图生图/姿势迁移-千问编辑2511_2003846907145428993.json, 图片生成/图生图/姿势迁移-千问编辑PLUS_1979763516292894722.json, 图片生成/图生图/通义千问姿势迁移_2003040280687329282.json, 图片生成/图生图/（电商流）qwen2509 edit 最强换姿势-姿势迁移-编辑放大修复4倍_1989558415099875329.json, 视频生成/图生视频/动作迁移-超高一致性 姿势参考-高清放大_2059442895932977153.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/ywt换姿势_2059923007493206018.json、图片生成/图生图/人物姿势参考图_2061617694088192001.json、图片生成/图生图/全自动换装+指定人脸 动作迁移_2070478132422987777.json、图片生成/图生图/全自动换装+指定人脸 动作迁移美图生成-超高一致性+高清输出+姿势可控+多图编辑+姿势参考-高清放大_2060190864319799298.json、图片生成/图生图/动作模仿全新调整版  人物姿势  姿势生成  姿势迁移  动作迁移_2078762792903077889.json…）

- **类型**：Image To Image
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 20 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 19/20 个有
- `SDPoseOODLoader` —— 17/20 个有
- `SDPoseOODProcessor` —— 17/20 个有
- `Get Image Size` —— 16/20 个有
- `GroundingDinoModelLoader_SDPose` —— 16/20 个有
- `Image Aspect Ratio` —— 16/20 个有
- `ImageResize` —— 16/20 个有
- `VAEEncodeTiled` —— 16/20 个有
- `YOLOModelLoader` —— 16/20 个有
- `ConditioningZeroOut` —— 4/20 个有
- `EmptySD3LatentImage` —— 4/20 个有
- `easy cleanGpuUsed` —— 4/20 个有
- `easy imageColorMatch` —— 4/20 个有
- `easy imageSize` —— 4/20 个有
- `DWPreprocessor` —— 3/20 个有
- `PathchSageAttentionKJ` —— 3/20 个有
- `Text` —— 3/20 个有
- `DepthAnythingV2Preprocessor` —— 2/20 个有
- `Fast Groups Bypasser (rgthree)` —— 2/20 个有
- `Any Switch (rgthree)` —— 1/20 个有
- `DrawViTPose` —— 1/20 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/20 个有
- `Label (rgthree)` —— 1/20 个有
- `OnnxDetectionModelLoader` —— 1/20 个有
- `PoseAndFaceDetection` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 20 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 20 | 100% |
| 采样算法 | euler | - | 20 | 85% |
| 调度器 | simple | - | 20 | 80% |
| 重绘幅度 | 0.3 | 0.3 - 1 | 20 | 37% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 41/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，20 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，20 个样本，一致性 85%
- 调度器 最常用 simple，20 个样本，一致性 80%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 1，20 个样本，取值分散，一致性仅 37%
- 高发问题（41/20 个样本）：Steps较低可能导致细节不足
