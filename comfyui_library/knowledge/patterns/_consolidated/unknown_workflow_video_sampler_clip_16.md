---
name: unknown_workflow_video_sampler_clip_16
type: Unknown Workflow
frequency: 22
level: strong
coverage: 0.635591
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_IntToFloat, GetImageRangeFromBatch, GetNode, ImageBatchMulti, ImageResizeKJv2, Int, KSampler, LoadImage, SetNode, SimpleMath+, TrimVideoLatent, VAEDecode, VAELoader, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/11characterreplacement_2048960943010353154.json, 图片生成/图生图/Wan2.2-Animate 跳舞打拳动作丝滑、不变背景 动作迁移，长视频稳定输出新标杆_1986748092575903745.json, 图片生成/图生图/Wan2.2-Animate-图生视频 官方原版更稳定 动作迁移（不变背景）+长视频 稳如老狗_1983452230231760897.json, 数字人/数字人/动作模仿（Animate）支持无限时长（手指稳定、支持更高分辨率）_2032027443770429442.json, 数字人/数字人/抖音 & 快手 AI 舞蹈视频（支持胸部抖动、超清、无限时长）Animate_2033906472924483586.json, 视频生成/图生视频/-图生视频（动作迁移+长视频）_2008225222398316546.json, 视频生成/图生视频/3-3Piao-动作迁移（一致性、表情、手部、抖动）Wan2.2-Animate-V5_2002747679463620610.json, 视频生成/图生视频/3-3动作迁移加速版_2020050725358804994.json, 视频生成/图生视频/Wan2.2-Animate-V5（一致性+表情+手部+抖动）_2037056894430351361.json, 视频生成/图生视频/Wan2.2-Animate-动作迁移 （长视频）表情+抖动+一致性+手部_2031640030707458050.json, 视频生成/图生视频/Wan2.2-Animate-动作迁移 （长视频）表情+抖动+一致性+手部_2071443164606586881.json, 视频生成/图生视频/Wan2.2-Animate-动作迁移_1995377555693875202.json, 视频生成/图生视频/动作模仿，动作复刻，舞蹈模仿，手指稳定、支持高分辨率_2033946576439218177.json, 视频生成/图生视频/动作模仿，自用版本_2051245118031704065.json, 视频生成/图生视频/动作迁移 V4（人物一致性、面部表情、对口型、肢体手部优化、🐻部抖动优化版）_2017780725273075713.json, 视频生成/图生视频/动作迁移+面部捕捉（精细版）_2052037112278593537.json, 视频生成/图生视频/动作迁移AnimateV2无表情参考版_2009276664982806530.json, 视频生成/图生视频/动作迁移全能版20260205_2019196248963682306.json, 视频生成/图生视频/动作迁移复刻-3Piao升级版+长视频人物一致性_2024093081133391873.json, 视频生成/图生视频/动作迁移（一致性、表情、胸部调节，手部、胸部抖动优化版）+0_2079778626383466497.json, 视频生成/图生视频/可用动作迁移（一致性、表情、手部、抖动）Wan2.2-Animate-V5_2064595503089807361.json, 视频生成/图生视频/可用动作迁移（一致性、表情、手部、抖动）_2052270105588973569.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_16

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/反推提示词/11characterreplacement_2048960943010353154.json、图片生成/图生图/Wan2.2-Animate 跳舞打拳动作丝滑、不变背景 动作迁移，长视频稳定输出新标杆_1986748092575903745.json、图片生成/图生图/Wan2.2-Animate-图生视频 官方原版更稳定 动作迁移（不变背景）+长视频 稳如老狗_1983452230231760897.json、数字人/数字人/动作模仿（Animate）支持无限时长（手指稳定、支持更高分辨率）_2032027443770429442.json、数字人/数字人/抖音 & 快手 AI 舞蹈视频（支持胸部抖动、超清、无限时长）Animate_2033906472924483586.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 22 个 workflow 都包含：
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
- `SetNode`
- `SimpleMath+`
- `TrimVideoLatent`
- `VAEDecode`
- `VAELoader`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 21/22 个有
- `ModelSamplingSD3` —— 21/22 个有
- `PreviewImage` —— 21/22 个有
- `UNETLoader` —— 21/22 个有
- `VHS_VideoInfoLoaded` —— 21/22 个有
- `PoseAndFaceDetection` —— 18/22 个有
- `Display Int (rgthree)` —— 17/22 个有
- `DrawViTPose` —— 17/22 个有
- `ImageScale` —— 17/22 个有
- `OnnxDetectionModelLoader` —— 17/22 个有
- `PathchSageAttentionKJ` —— 14/22 个有
- `Primitive integer [Crystools]` —— 14/22 个有
- `easy float` —— 13/22 个有
- `BatchCount+` —— 8/22 个有
- `ImageBatch` —— 8/22 个有
- `ImageFromBatch` —— 8/22 个有
- `RepeatImageBatch` —— 8/22 个有
- `easy mathInt` —— 8/22 个有
- `DWPreprocessor` —— 5/22 个有
- `RHHiddenNodes` —— 5/22 个有
- `ImageConcanate` —— 1/22 个有
- `LayerUtility: PurgeVRAM V2` —— 1/22 个有
- `Notif-PlaySound` —— 1/22 个有
- `PixelPerfectResolution` —— 1/22 个有
- `RIFE VFI` —— 1/22 个有
- `RMBG` —— 1/22 个有
- `RTXVideoSuperResolution` —— 1/22 个有
- `SaveImage` —— 1/22 个有
- `ShellAgentPluginSaveAudios` —— 1/22 个有
- `TT_img_enc` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 22 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 22 | 100% |
| 采样算法 | euler | - | 22 | 100% |
| 调度器 | simple | - | 22 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 69/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，22 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，22 个样本，一致性 100%
- 调度器 最常用 simple，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 高发问题（69/22 个样本）：Steps较低可能导致细节不足
