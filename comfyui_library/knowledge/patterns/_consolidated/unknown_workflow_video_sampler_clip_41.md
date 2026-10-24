---
name: unknown_workflow_video_sampler_clip_41
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.935083
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJv2, ImpactInt, KSamplerAdvanced, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveStringMultiline, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/图生视频 高动态 Smooth Mix  Wan 2.2_1979531861057769474.json, 视频生成/图生视频/最强电商女装丝滑带货文图生视频工作流_2050045558773035009.json, 视频生成/图生视频/电影时光机+爆款复刻+多图首尾帧_2007316422707388418.json, 视频生成/图生视频/视频生成-生成视频片段_2010181863981191170.json, 视频生成/图生视频/视频生成-生成视频片段_2012343495582818305.json, 视频生成/图生视频/飞行魔法少女+飞行滑板+多图首尾帧_2006937829007433729.json, 视频生成/图生视频/首尾帧图生视频Wan2.2-Smooth Mix 超丝滑动态电影感画质极速渲染 工作流_1981312323858104321.json, 视频生成/图生视频/首尾帧视频_1986671035942662146.json, 视频生成/图生视频/高动态电影级首尾帧Wan2.2-Smooth Mix 超丝滑动态1.0_1986030132559314946.json, 视频生成/图生视频/🚵Smooth Mix wan2.2 高动态电影质感模型 图生视频🚵_1979384591175815170.json, 视频生成/图生视频/🚵Smooth Mix wan2.2 高动态电影质感模型 首尾帧视频🚵_1979384908328112130.json, 视频生成/文生视频/高动态电影探班短视频复刻首尾帧Wan2.2-Smooth Mix_1999803744537673729.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_41

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/图生视频 高动态 Smooth Mix  Wan 2.2_1979531861057769474.json、视频生成/图生视频/最强电商女装丝滑带货文图生视频工作流_2050045558773035009.json、视频生成/图生视频/电影时光机+爆款复刻+多图首尾帧_2007316422707388418.json、视频生成/图生视频/视频生成-生成视频片段_2010181863981191170.json、视频生成/图生视频/视频生成-生成视频片段_2012343495582818305.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `ImpactInt`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Seed (rgthree)` —— 11/12 个有
- `easy cleanGpuUsed` —— 11/12 个有
- `Fast Bypasser (rgthree)` —— 10/12 个有
- `Mute / Bypass Repeater (rgthree)` —— 10/12 个有
- `wanBlockSwap` —— 10/12 个有
- `RIFE VFI` —— 9/12 个有
- `ImageScaleBy` —— 8/12 个有
- `WanFirstLastFrameToVideo` —— 5/12 个有
- `WanImageToVideo` —— 5/12 个有
- `RHHiddenNodes` —— 4/12 个有
- `GetNode` —— 2/12 个有
- `Note Plus (mtb)` —— 2/12 个有
- `SetNode` —— 2/12 个有
- `WanAdvancedI2V` —— 2/12 个有
- `ImageResize+` —— 1/12 个有
- `RH_LLMAPI_NODE` —— 1/12 个有
- `RH_Nano_Banana_Image2Image` —— 1/12 个有
- `RH_Translator` —— 1/12 个有
- `SaveImage` —— 1/12 个有
- `ShowText` —— 1/12 个有
- `easy textSwitch` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 12 | 75% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 12 | 100% |
| 采样算法 | 1 | 1 - 1 | 12 | 100% |
| 调度器 | euler_ancestral | - | 12 | 100% |
| 重绘幅度 | simple | - | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，12 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，12 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，12 个样本，一致性 100%
- 重绘幅度 最常用 simple，12 个样本，一致性 100%
