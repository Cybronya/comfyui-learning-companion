---
name: unknown_workflow_video_lora_sampler_386
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.777667
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Model Input Switch, DrawMaskOnImage, DrawViTPose, Fast Bypasser (rgthree), GetNode, GrowMask, ImageBlend, ImageConcatMulti, ImageResizeKJv2, ImpactInt, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), OnnxDetectionModelLoader, PathchSageAttentionKJ, PointsEditor, PoseAndFaceDetection, PreviewImage, PrimitiveFloat, SeCModelLoader, SeCVideoSegmentation, SetNode, SimpleMath+, TorchCompileModelWanVideoV2, TrimVideoLatent, UNETLoader, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo, easy convertAnything, easy int, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【视频换人】Animate +Sec扣图换人_1978713604222554114.json, 图片生成/文生图/Animate 动作迁移 人物替换 终极整合官方版 新遮罩 更精准_1978479937873137665.json, 数字人/数字人/Animate 动作迁移 人物替换 终极整合官方版 新遮罩 更精准1026_1980923631545044993.json, 视频生成/图生视频/Animate +Sec扣图节点 --动作迁移、人物替换 -- 想换哪里换哪里_1979733703280726017.json, 视频生成/图生视频/Animate 动作迁移 人物替换 终极整合官方版 新遮罩 更精准_1977883468296245249.json, 视频生成/图生视频/最新Wan Animate 动作迁移+人物替换  新遮罩SEC 更精准 想换哪换哪_1980798178817654785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_386

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/【视频换人】Animate +Sec扣图换人_1978713604222554114.json、图片生成/文生图/Animate 动作迁移 人物替换 终极整合官方版 新遮罩 更精准_1978479937873137665.json、数字人/数字人/Animate 动作迁移 人物替换 终极整合官方版 新遮罩 更精准1026_1980923631545044993.json、视频生成/图生视频/Animate +Sec扣图节点 --动作迁移、人物替换 -- 想换哪里换哪里_1979733703280726017.json、视频生成/图生视频/Animate 动作迁移 人物替换 终极整合官方版 新遮罩 更精准_1977883468296245249.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 6 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Model Input Switch`
- `DrawMaskOnImage`
- `DrawViTPose`
- `Fast Bypasser (rgthree)`
- `GetNode`
- `GrowMask`
- `ImageBlend`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `ImpactInt`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `Mute / Bypass Repeater (rgthree)`
- `OnnxDetectionModelLoader`
- `PathchSageAttentionKJ`
- `PointsEditor`
- `PoseAndFaceDetection`
- `PreviewImage`
- `PrimitiveFloat`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SetNode`
- `SimpleMath+`
- `TorchCompileModelWanVideoV2`
- `TrimVideoLatent`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `easy convertAnything`
- `easy int`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 2/6 个有
- `ImageResizeKJ` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | sa_solver | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
