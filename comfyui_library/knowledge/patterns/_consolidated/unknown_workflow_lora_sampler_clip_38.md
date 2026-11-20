---
name: unknown_workflow_lora_sampler_clip_38
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.5478
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [数字人/数字人/Berinini版-无限时长-带货数字人替换_2074707187401838593.json, 视频生成/图生视频/Bernini 角色替换_2069319914443333634.json, 视频生成/图生视频/video_wan2_2_bernini_rv2v_add_2064247414655115266.json, 视频生成/图生视频/video_wan2_2_bernini_rv2v_replace_2064232122084319234.json, 视频生成/图生视频/video_wan2_2_with_skill_prompt_2013644132241121282.json, 视频生成/文生视频/video_wan2_2_bernini_i2i_2064270918700060673.json, 视频生成/文生视频/video_wan2_2_bernini_multi_r2v_2064268091416207362.json, 视频生成/文生视频/video_wan2_2_bernini_r2v_2064265816681570306.json, 视频生成/文生视频/video_wan2_2_bernini_rv2v_change_style_2064258770699636737.json, 视频生成/文生视频/video_wan2_2_bernini_rv2v_changebg_2064251615900688385.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_38

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/Berinini版-无限时长-带货数字人替换_2074707187401838593.json、视频生成/图生视频/Bernini 角色替换_2069319914443333634.json、视频生成/图生视频/video_wan2_2_bernini_rv2v_add_2064247414655115266.json、视频生成/图生视频/video_wan2_2_bernini_rv2v_replace_2064232122084319234.json、视频生成/图生视频/video_wan2_2_with_skill_prompt_2013644132241121282.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：55%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BerniniConditioning` —— 9/10 个有
- `ModelSamplingSD3` —— 9/10 个有
- `VHS_LoadVideo` —— 9/10 个有
- `VHS_VideoCombine` —— 9/10 个有
- `WanVideoNAG` —— 9/10 个有
- `CFGZeroStar` —— 8/10 个有
- `CLIPVisionLoader` —— 8/10 个有
- `GetNode` —— 8/10 个有
- `SetNode` —— 8/10 个有
- `BatchImagesNode` —— 7/10 个有
- `CLIPVisionEncode` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `SimpleMath+` —— 1/10 个有
- `VHS_VideoInfoLoaded` —— 1/10 个有
- `WanContextWindowsManual` —— 1/10 个有
- `WanImageToVideo` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 10 | 70% |
| Prompt 约束强度(CFG) | 6 | 6 - 10 | 10 | 81% |
| 采样算法 | 1 | 1 - 1 | 10 | 100% |
| 调度器 | lcm | - | 10 | 80% |
| 重绘幅度 | simple | - | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，10 个样本，一致性 70%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 10，10 个样本，取值集中（一致性 81%）
- 采样算法 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，10 个样本，一致性 80%
- 重绘幅度 最常用 simple，10 个样本，一致性 100%
