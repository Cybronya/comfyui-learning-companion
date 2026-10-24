---
name: unknown_workflow_video_clip_unet_2
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.97625
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJv2, ImpactInt, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/YJ-APP-首尾帧  Smooth Mix Wan 2.2_2038638584823029761.json, 图片生成/图生图/YJ-APP-首尾帧  Wan 2.2_2041525838901940226.json, 视频生成/图生视频/004.Wan视频之源002.首尾帧图生视频超丝滑极速渲染_2035302183196954625.json, 视频生成/图生视频/Smooth Mix wan2.2 电影质画质-加速版+动态升级+视频放大-图生视频-V2_1989316468380717058.json, 视频生成/图生视频/Wan2.2-Smooth Mix飞行少女飞行滑板多图首尾帧图生视频 超丝滑首尾帧工作流_2079544662850887682.json, 视频生成/图生视频/Wan2.2-Smooth Mix飞行少女飞行滑板多图首尾帧图生视频 超丝滑首尾帧工作流_2087859368317505538.json, 视频生成/图生视频/[众馨]wan2.2首尾帧_2001506323961397250.json, 视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_2010998394537381889.json, 视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_2035897809894903809.json, 视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_2039617670403858433.json, 视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_2041028074229211137.json, 视频生成/图生视频/公路飞行短视频复刻Wan2.2-Smooth+Mix_2004910059593367554.json, 视频生成/图生视频/图生视频_1986278808032595970.json, 视频生成/图生视频/视频全能融合模型Smooth Mix wan2.2_1979453083128336385.json, 视频生成/图生视频/飞行少女飞行滑板多图首尾帧图生视频Wan2.2-Smooth Mix 超丝滑首尾帧工作流_2055911477286064130.json, 视频生成/图生视频/飞行少女飞行滑板多图首尾帧图生视频：Wan2.2-Smooth Mix超丝滑首尾帧图生视频工作流_2017823753580847106.json, 视频生成/图生视频/飞行少女飞行滑板多图首尾帧首尾帧图生视频Wan2.2-Smooth Mix 超丝滑首尾帧工作流_2011515988684050433.json, 视频生成/图生视频/飞行少女飞行滑板多图首尾帧首尾帧图生视频Wan2.2-Smooth Mix 超丝滑首尾帧工作流_2103812745828327426.json, 视频生成/图生视频/飞行魔法少女+飞行滑板+多图首尾帧_2005234314344361986.json, 视频生成/图生视频/🚵Smooth Mix wan2.2 高动态电影质感模型 图生视频【动态升级版V2】🚵_1988422481260232705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_2

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/YJ-APP-首尾帧  Smooth Mix Wan 2.2_2038638584823029761.json、图片生成/图生图/YJ-APP-首尾帧  Wan 2.2_2041525838901940226.json、视频生成/图生视频/004.Wan视频之源002.首尾帧图生视频超丝滑极速渲染_2035302183196954625.json、视频生成/图生视频/Smooth Mix wan2.2 电影质画质-加速版+动态升级+视频放大-图生视频-V2_1989316468380717058.json、视频生成/图生视频/Wan2.2-Smooth Mix飞行少女飞行滑板多图首尾帧图生视频 超丝滑首尾帧工作流_2079544662850887682.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `ImpactInt`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 18/20 个有
- `Seed (rgthree)` —— 18/20 个有
- `easy cleanGpuUsed` —— 18/20 个有
- `wanBlockSwap` —— 18/20 个有
- `Fast Bypasser (rgthree)` —— 17/20 个有
- `ImageScaleBy` —— 17/20 个有
- `Mute / Bypass Repeater (rgthree)` —— 17/20 个有
- `PrimitiveStringMultiline` —— 17/20 个有
- `RIFE VFI` —— 17/20 个有
- `WanFirstLastFrameToVideo` —— 13/20 个有
- `ImageBatchExtendWithOverlap` —— 7/20 个有
- `WanAdvancedI2V` —— 7/20 个有
- `WanImageToVideo` —— 6/20 个有
- `CR Text` —— 2/20 个有
- `LoraLoaderModelOnly` —— 2/20 个有
- `PainterI2V` —— 2/20 个有
- `WanMoeKSampler` —— 2/20 个有
- `Fast Groups Bypasser (rgthree)` —— 1/20 个有
- `Int` —— 1/20 个有
- `Note Plus (mtb)` —— 1/20 个有
- `Switch` —— 1/20 个有
- `Text` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 20 | 50% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 20 | 100% |
| 采样算法 | 1 | 1 - 1 | 20 | 100% |
| 调度器 | euler_ancestral | - | 20 | 90% |
| 重绘幅度 | simple | - | 20 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，20 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，20 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，20 个样本，一致性 90%
- 重绘幅度 最常用 simple，20 个样本，一致性 90%
