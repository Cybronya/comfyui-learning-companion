---
name: unknown_workflow_video_lora_sampler_156
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.842727
common_nodes: [CLIPLoader, CLIPVisionLoader, DrawViTPose, ImageFromBatch, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, OnnxDetectionModelLoader, PoseAndFaceDetection, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/AI换装｜Qwen Edit＋Wan2.2 Animate｜动作迁移视频_2100460302033838082.json, 视频生成/图生视频/动作迁移+服装换装+服装带货_2084132243286614018.json, 视频生成/图生视频/口哨舞-手势舞-换衣+动作迁移+抖X+最长30秒_2091127654450819073.json, 视频生成/图生视频/换衣+动作迁移+抖X_2091117455124029442.json, 视频生成/图生视频/换衣+动作迁移+抖X_2109943597553512449.json, 视频生成/图生视频/2065961484110360577.json, 视频生成/图生视频/换装+迁移+服装带货_2082823806179168258.json, 视频生成/图生视频/换装+迁移+服装带货（流量密码版）_2083093296070610945.json, 视频生成/图生视频/换装+迁移+服装带货（流量密码版）_2083875222989656066.json, 视频生成/图生视频/短视频人物服装高清替换+电商换装+尺度版_2088577100151345153.json, 视频生成/文生视频/换装+迁移+服装带货（流量密码版）_2083875222989656066.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_156

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/AI换装｜Qwen Edit＋Wan2.2 Animate｜动作迁移视频_2100460302033838082.json、视频生成/图生视频/动作迁移+服装换装+服装带货_2084132243286614018.json、视频生成/图生视频/口哨舞-手势舞-换衣+动作迁移+抖X+最长30秒_2091127654450819073.json、视频生成/图生视频/换衣+动作迁移+抖X_2091117455124029442.json、视频生成/图生视频/换衣+动作迁移+抖X_2109943597553512449.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPVisionLoader`
- `DrawViTPose`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 9/11 个有
- `CropWithPadInfo` —— 9/11 个有
- `Fast Groups Muter (rgthree)` —— 9/11 个有
- `Image Comparer (rgthree)` —— 9/11 个有
- `PrimitiveStringMultiline` —— 9/11 个有
- `QwenEditConfigPreparer` —— 9/11 个有
- `QwenEditOutputExtractor` —— 9/11 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 9/11 个有
- `easy imageRemBg` —— 9/11 个有
- `GetNode` —— 7/11 个有
- `ImageUpscaleWithModel` —— 7/11 个有
- `JWInteger` —— 7/11 个有
- `LayerUtility: PurgeVRAM` —— 7/11 个有
- `PrimitiveInt` —— 7/11 个有
- `SetNode` —— 7/11 个有
- `SimpleMath+` —— 7/11 个有
- `UpscaleModelLoader` —— 7/11 个有
- `ttN float` —— 7/11 个有
- `BatchCount+` —— 4/11 个有
- `ComfyMathExpression` —— 4/11 个有
- `ImageBatch` —— 4/11 个有
- `Int` —— 4/11 个有
- `MemoryCleaner` —— 4/11 个有
- `PreviewImage` —— 4/11 个有
- `RepeatImageBatch` —— 4/11 个有
- `WanVideoLoraSelect` —— 4/11 个有
- `easy mathInt` —— 4/11 个有
- `孤海注释` —— 3/11 个有
- `ConditioningZeroOut` —— 2/11 个有
- `GoohaiUniversalSlider` —— 2/11 个有
- `SaveImage` —— 2/11 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/11 个有
- `CR Text` —— 1/11 个有
- `Float` —— 1/11 个有
- `Primitive integer [Crystools]` —— 1/11 个有
- `easy float` —— 1/11 个有
- `easy int` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | beta57 | - | 11 | 82% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 beta57，11 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
