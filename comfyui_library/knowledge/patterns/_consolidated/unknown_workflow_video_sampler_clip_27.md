---
name: unknown_workflow_video_sampler_clip_27
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.972714
common_nodes: [CLIPLoader, CLIPTextEncode, ImpactInt, KSamplerAdvanced, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1985980018524336129.json, 视频生成/图生视频/2004910059593367554.json, 视频生成/图生视频/1986278808032595970.json, 视频生成/图生视频/2053671434622386177.json, 视频生成/图生视频/2007316422707388418.json, 视频生成/图生视频/2010181863981191170.json, 视频生成/图生视频/2012343495582818305.json, 视频生成/图生视频/2006937829007433729.json, 视频生成/图生视频/1981312323858104321.json, 视频生成/图生视频/1986671035942662146.json, 视频生成/图生视频/1986030132559314946.json, 视频生成/图生视频/1979384591175815170.json, 视频生成/图生视频/1979384908328112130.json, 视频生成/文生视频/高动态电影探班短视频复刻首尾帧Wan2.2-Smooth Mix_1999803744537673729.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_27

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/1985980018524336129.json、视频生成/图生视频/2004910059593367554.json、视频生成/图生视频/1986278808032595970.json、视频生成/图生视频/2053671434622386177.json、视频生成/图生视频/2007316422707388418.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImpactInt`
- `KSamplerAdvanced`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 13/14 个有
- `CLIPVisionLoader` —— 13/14 个有
- `Fast Bypasser (rgthree)` —— 13/14 个有
- `ImageResizeKJv2` —— 13/14 个有
- `Mute / Bypass Repeater (rgthree)` —— 13/14 个有
- `PrimitiveStringMultiline` —— 13/14 个有
- `Seed (rgthree)` —— 13/14 个有
- `easy cleanGpuUsed` —— 13/14 个有
- `LoadImage` —— 12/14 个有
- `wanBlockSwap` —— 12/14 个有
- `ImageScaleBy` —— 10/14 个有
- `RIFE VFI` —— 10/14 个有
- `WanFirstLastFrameToVideo` —— 7/14 个有
- `RHHiddenNodes` —— 5/14 个有
- `WanImageToVideo` —— 5/14 个有
- `LoraLoaderModelOnly` —— 2/14 个有
- `Note Plus (mtb)` —— 2/14 个有
- `WanAdvancedI2V` —— 2/14 个有
- `ImageLoader` —— 1/14 个有
- `ImageResize+` —— 1/14 个有
- `RH_Nano_Banana_Image2Image` —— 1/14 个有
- `RH_Translator` —— 1/14 个有
- `RTXVideoSuperResolution` —— 1/14 个有
- `SaveImage` —— 1/14 个有
- `ShowText` —— 1/14 个有
- `easy positive` —— 1/14 个有
- `easy showAnything` —— 1/14 个有
- `llama_cpp_instruct_adv` —— 1/14 个有
- `llama_cpp_model_loader` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 14 | 79% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 14 | 92% |
| 采样算法 | 1 | 1 - 1 | 14 | 100% |
| 调度器 | euler_ancestral | - | 14 | 100% |
| 重绘幅度 | simple | - | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，14 个样本，一致性 79%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，14 个样本，取值集中（一致性 92%）
- 采样算法 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，14 个样本，一致性 100%
- 重绘幅度 最常用 simple，14 个样本，一致性 100%
