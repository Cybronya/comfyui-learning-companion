---
name: unknown_workflow_video_lora_sampler_256
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7381
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetNode, GrowMask, ImageBlend, ImageConcatMulti, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, OnnxDetectionModelLoader, PointsEditor, PoseAndFaceDetection, PreviewImage, SeCModelLoader, SeCVideoSegmentation, SetNode, TrimVideoLatent, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo, easy int, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【视频换人】Animate +Sec扣图换人_1978713604222554114.json, 图片生成/文生图/Animate 动作迁移 人物替换 终极整合官方版 新遮罩 更精准_1978479937873137665.json, 平台全量/AI代码侠土豆-Wan2_2_Animate-Q8+Sec_4B（极速）_1977928233163390977.json, 平台全量/Animate +Sec扣图节点 --动作迁移、人物替换 -- 想换哪里换哪里_1978429597777809410.json, 平台全量/Animate +Sec扣图节点 --动作迁移（背景不换）_1978796447749541890.json, 平台全量/Animate 动作迁移 人物替换 终极整合官方版 新遮罩 更精准_1980258297108475906.json, 数字人/数字人/Animate 动作迁移 人物替换 终极整合官方版 新遮罩 更精准1026_1980923631545044993.json, 视频生成/图生视频/Animate +Sec扣图节点 --动作迁移、人物替换 -- 想换哪里换哪里_1979733703280726017.json, 视频生成/图生视频/Animate 动作迁移 人物替换 终极整合官方版 新遮罩 更精准_1977883468296245249.json, 视频生成/图生视频/最新Wan Animate 动作迁移+人物替换  新遮罩SEC 更精准 想换哪换哪_1980798178817654785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_256

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/【视频换人】Animate +Sec扣图换人_1978713604222554114.json、图片生成/文生图/Animate 动作迁移 人物替换 终极整合官方版 新遮罩 更精准_1978479937873137665.json、平台全量/AI代码侠土豆-Wan2_2_Animate-Q8+Sec_4B（极速）_1977928233163390977.json、平台全量/Animate +Sec扣图节点 --动作迁移、人物替换 -- 想换哪里换哪里_1978429597777809410.json、平台全量/Animate +Sec扣图节点 --动作迁移（背景不换）_1978796447749541890.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 10 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetNode`
- `GrowMask`
- `ImageBlend`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `OnnxDetectionModelLoader`
- `PointsEditor`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SetNode`
- `TrimVideoLatent`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `easy int`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `CR Model Input Switch` —— 9/10 个有
- `Fast Bypasser (rgthree)` —— 9/10 个有
- `ImpactInt` —— 9/10 个有
- `LayerUtility: PurgeVRAM` —— 9/10 个有
- `ModelPatchTorchSettings` —— 9/10 个有
- `Mute / Bypass Repeater (rgthree)` —— 9/10 个有
- `PathchSageAttentionKJ` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `SimpleMath+` —— 9/10 个有
- `TorchCompileModelWanVideoV2` —— 9/10 个有
- `UNETLoader` —— 9/10 个有
- `easy convertAnything` —— 9/10 个有
- `JjkText` —— 4/10 个有
- `ImageResizeKJ` —— 1/10 个有
- `Note Plus (mtb)` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | sa_solver | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
