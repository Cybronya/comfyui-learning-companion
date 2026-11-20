---
name: unknown_workflow_video_lora_sampler_164
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.636571
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_IntToFloat, GetImageRangeFromBatch, GetNode, ImageBatchMulti, ImageResizeKJv2, Int, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SetNode, SimpleMath+, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/-图生视频（动作迁移+长视频）_2008225222398316546.json, 视频生成/图生视频/3-3动作迁移加速版_2020050725358804994.json, 视频生成/图生视频/Wan2.2-Animate-V5（一致性+表情+手部+抖动）_2037056894430351361.json, 视频生成/图生视频/Wan2.2-Animate-动作迁移 （长视频）表情+抖动+一致性+手部_2031640030707458050.json, 视频生成/图生视频/Wan2.2-Animate-动作迁移 （长视频）表情+抖动+一致性+手部_2071443164606586881.json, 视频生成/图生视频/Wan2.2-Animate-动作迁移_1995377555693875202.json, 视频生成/图生视频/Wan2.2-Animate-图生视频（动作迁移+长视频）_1973274759364521985.json, 视频生成/图生视频/动作模仿，动作复刻，舞蹈模仿，手指稳定、支持高分辨率_2033946576439218177.json, 视频生成/图生视频/动作模仿，自用版本_2051245118031704065.json, 视频生成/图生视频/动作迁移AnimateV2无表情参考版_2009276664982806530.json, 视频生成/图生视频/动作迁移复刻-3Piao升级版+长视频人物一致性_2024093081133391873.json, 视频生成/图生视频/可用动作迁移（一致性、表情、手部、抖动）Wan2.2-Animate-V5_2064595503089807361.json, 视频生成/图生视频/可用动作迁移（一致性、表情、手部、抖动）_2052270105588973569.json, 视频生成/图生视频/超稳定 720x1280P Wan2.2超清 美女跳舞 动作迁移 表情+口型复刻_2017778215057629185.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_164

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/-图生视频（动作迁移+长视频）_2008225222398316546.json、视频生成/图生视频/3-3动作迁移加速版_2020050725358804994.json、视频生成/图生视频/Wan2.2-Animate-V5（一致性+表情+手部+抖动）_2037056894430351361.json、视频生成/图生视频/Wan2.2-Animate-动作迁移 （长视频）表情+抖动+一致性+手部_2031640030707458050.json、视频生成/图生视频/Wan2.2-Animate-动作迁移 （长视频）表情+抖动+一致性+手部_2071443164606586881.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CM_IntToFloat`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `Int`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `SetNode`
- `SimpleMath+`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoInfoLoaded` —— 13/14 个有
- `Display Int (rgthree)` —— 11/14 个有
- `DrawViTPose` —— 11/14 个有
- `ImageScale` —— 11/14 个有
- `OnnxDetectionModelLoader` —— 11/14 个有
- `PoseAndFaceDetection` —— 11/14 个有
- `Primitive integer [Crystools]` —— 10/14 个有
- `PathchSageAttentionKJ` —— 9/14 个有
- `easy float` —— 9/14 个有
- `BatchCount+` —— 7/14 个有
- `ImageBatch` —— 7/14 个有
- `ImageFromBatch` —— 7/14 个有
- `RepeatImageBatch` —— 7/14 个有
- `easy mathInt` —— 7/14 个有
- `DWPreprocessor` —— 3/14 个有
- `RHHiddenNodes` —— 3/14 个有
- `ImageConcanate` —— 1/14 个有
- `PixelPerfectResolution` —— 1/14 个有
- `SaveImage` —— 1/14 个有
- `TT_img_enc` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 14 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 42/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（42/14 个样本）：Steps较低可能导致细节不足
