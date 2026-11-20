---
name: unknown_workflow_video_clip_unet
type: Unknown Workflow
frequency: 19
level: strong
coverage: 0.973789
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJv2, ImpactInt, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/YJ-APP-首尾帧  Smooth Mix Wan 2.2_2038638584823029761.json, 图片生成/图生图/YJ-APP-首尾帧  Wan 2.2_2041525838901940226.json, 平台全量/💨S-MIX子弹旋转特效💨_1984704184287117314.json, 视频生成/图生视频/004.Wan视频之源002.首尾帧图生视频超丝滑极速渲染_2035302183196954625.json, 视频生成/图生视频/Smooth Mix wan2.2 电影质画质-加速版+动态升级+视频放大-图生视频-V2_1989316468380717058.json, 视频生成/图生视频/Smooth wan2.2 电影质感视频生成_1983826871899070465.json, 视频生成/图生视频/Wan2.2 Smooth Mix 高动态电影质感 图生视频_1982107238137511938.json, 视频生成/图生视频/Wan2.2 Smooth Mix 高动态电影质感 首尾帧视频_1981536473277177858.json, 视频生成/图生视频/Wan2.2 Smooth Mix 高动态电影质感 首尾帧视频_2011239621144875009.json, 视频生成/图生视频/Wan2.2-Smooth Mix 超丝滑动态电影感画质极速渲染 图生视频工作流_1981294713347145729.json, 视频生成/图生视频/Wan2.2-Smooth Mix飞行少女飞行滑板多图首尾帧图生视频 超丝滑首尾帧工作流_2079544662850887682.json, 视频生成/图生视频/Wan2.2-Smooth Mix飞行少女飞行滑板多图首尾帧图生视频 超丝滑首尾帧工作流_2087859368317505538.json, 视频生成/图生视频/[众馨]wan2.2首尾帧_2001506323961397250.json, 视频生成/图生视频/飞行少女飞行滑板多图首尾帧图生视频Wan2.2-Smooth Mix 超丝滑首尾帧工作流_2055911477286064130.json, 视频生成/图生视频/飞行少女飞行滑板多图首尾帧图生视频：Wan2.2-Smooth Mix超丝滑首尾帧图生视频工作流_2017823753580847106.json, 视频生成/图生视频/飞行少女飞行滑板多图首尾帧首尾帧图生视频Wan2.2-Smooth Mix 超丝滑首尾帧工作流_2011515988684050433.json, 视频生成/图生视频/飞行少女飞行滑板多图首尾帧首尾帧图生视频Wan2.2-Smooth Mix 超丝滑首尾帧工作流_2103812745828327426.json, 视频生成/图生视频/飞行魔法少女+飞行滑板+多图首尾帧_2005234314344361986.json, 视频生成/图生视频/🚵Smooth Mix wan2.2 高动态电影质感模型 图生视频【动态升级版V2】🚵_1988422481260232705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/YJ-APP-首尾帧  Smooth Mix Wan 2.2_2038638584823029761.json、图片生成/图生图/YJ-APP-首尾帧  Wan 2.2_2041525838901940226.json、平台全量/💨S-MIX子弹旋转特效💨_1984704184287117314.json、视频生成/图生视频/004.Wan视频之源002.首尾帧图生视频超丝滑极速渲染_2035302183196954625.json、视频生成/图生视频/Smooth Mix wan2.2 电影质画质-加速版+动态升级+视频放大-图生视频-V2_1989316468380717058.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `ImpactInt`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 18/19 个有
- `wanBlockSwap` —— 18/19 个有
- `Fast Bypasser (rgthree)` —— 17/19 个有
- `KSamplerAdvanced` —— 17/19 个有
- `RIFE VFI` —— 17/19 个有
- `Seed (rgthree)` —— 17/19 个有
- `easy cleanGpuUsed` —— 17/19 个有
- `ImageScaleBy` —— 16/19 个有
- `Mute / Bypass Repeater (rgthree)` —— 16/19 个有
- `PrimitiveStringMultiline` —— 16/19 个有
- `WanFirstLastFrameToVideo` —— 13/19 个有
- `ImageBatchExtendWithOverlap` —— 7/19 个有
- `WanAdvancedI2V` —— 7/19 个有
- `WanImageToVideo` —— 4/19 个有
- `CR Text` —— 2/19 个有
- `LoraLoaderModelOnly` —— 2/19 个有
- `PainterI2V` —— 2/19 个有
- `WanMoeKSampler` —— 2/19 个有
- `easy float` —— 2/19 个有
- `FlashVSRNode` —— 1/19 个有
- `Int` —— 1/19 个有
- `Note Plus (mtb)` —— 1/19 个有
- `Switch` —— 1/19 个有
- `Text` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 19 | 58% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 19 | 100% |
| 采样算法 | 1 | 1 - 1 | 19 | 100% |
| 调度器 | euler_ancestral | - | 19 | 89% |
| 重绘幅度 | simple | - | 19 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，19 个样本，一致性 58%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，19 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，19 个样本，一致性 89%
- 重绘幅度 最常用 simple，19 个样本，一致性 89%
