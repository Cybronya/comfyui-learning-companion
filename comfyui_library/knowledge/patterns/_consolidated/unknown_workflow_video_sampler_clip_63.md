---
name: unknown_workflow_video_sampler_clip_63
type: Unknown Workflow
frequency: 10
level: weak
coverage: 0.975
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResizeKJv2, KSamplerAdvanced, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2图生视频动态加强-PainterI2V_1988236119332536321.json, "视频生成/图生视频/Wan2.2官方ComfyUI图生视频,高质量生成细节把控_1951292355926282242.json", 视频生成/图生视频/YJ-APP-Wan2.2-Smooth-I2V_2038634972579373058.json, 视频生成/图生视频/wan2.2 Smooth Mix 高级电影质感和短剧—— 图生视频_1980633692215361538.json, 视频生成/图生视频/wan2.2 图生视频_2006925723407228930.json, 视频生成/图生视频/wan2.2 首帧图生视频字字1080_2018657772811853825.json, 视频生成/图生视频/wan2.2 首帧图生视频字字720_2018729929084510209.json, 视频生成/图生视频/一键生成花材展示电商短视频_2009598515076407298.json, 视频生成/图生视频/电影探班-爆款复刻-简单易用-优化版效果最好-独家原创工作流_2009284920207745026.json, 视频生成/图生视频/视频-您与建筑大师的动态合影工作流_2017792462663716865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_63

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Wan2.2图生视频动态加强-PainterI2V_1988236119332536321.json、视频生成/图生视频/Wan2.2官方ComfyUI图生视频,高质量生成细节把控_1951292355926282242.json、视频生成/图生视频/YJ-APP-Wan2.2-Smooth-I2V_2038634972579373058.json、视频生成/图生视频/wan2.2 Smooth Mix 高级电影质感和短剧—— 图生视频_1980633692215361538.json、视频生成/图生视频/wan2.2 图生视频_2006925723407228930.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 9/10 个有
- `CLIPVisionLoader` —— 9/10 个有
- `PathchSageAttentionKJ` —— 9/10 个有
- `easy cleanGpuUsed` —— 9/10 个有
- `ImpactInt` —— 8/10 个有
- `ModelPatchTorchSettings` —— 8/10 个有
- `Seed (rgthree)` —— 8/10 个有
- `SimpleMath+` —— 8/10 个有
- `WanImageToVideo` —— 7/10 个有
- `Fast Bypasser (rgthree)` —— 5/10 个有
- `Mute / Bypass Repeater (rgthree)` —— 5/10 个有
- `PrimitiveStringMultiline` —— 5/10 个有
- `wanBlockSwap` —— 5/10 个有
- `ImageScaleBy` —— 4/10 个有
- `RIFE VFI` —— 4/10 个有
- `LoadAudio` —— 3/10 个有
- `RHHiddenNodes` —— 3/10 个有
- `WanFirstLastFrameToVideo` —— 3/10 个有
- `JWInteger` —— 2/10 个有
- `easy anythingIndexSwitch` —— 2/10 个有
- `easy batchAnything` —— 2/10 个有
- `easy forLoopEnd` —— 2/10 个有
- `easy forLoopStart` —— 2/10 个有
- `CR Text Concatenate` —— 1/10 个有
- `ImageBatchGet` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `PainterI2V` —— 1/10 个有
- `TextInput_` —— 1/10 个有
- `easy imageSplitGrid` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 10 | 60% |
| Prompt 约束强度(CFG) | 7 | 4 - 20 | 10 | 42% |
| 采样算法 | 1 | 1 - 3.5 | 10 | 40% |
| 调度器 | euler_ancestral | - | 10 | 60% |
| 重绘幅度 | simple | - | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，10 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 7，观测区间 4 - 20，10 个样本，取值分散，一致性仅 42%
- 采样算法 中位数 1，观测区间 1 - 3.5，10 个样本，取值分散，一致性仅 40%
- 调度器 最常用 euler_ancestral，10 个样本，一致性 60%
- 重绘幅度 最常用 simple，10 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
