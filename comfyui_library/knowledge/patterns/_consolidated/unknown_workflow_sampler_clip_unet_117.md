---
name: unknown_workflow_sampler_clip_unet_117
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.882333
common_nodes: [BasicScheduler, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/hunyuan_video_text_to_video.json, 图片生成/文生图/文生视频加速版_1993105222903988226.json, 图片生成/文生图/混元T2V官方工作流_文生视频_1930244657111011329.json, 视频生成/图生视频/8步FAST快速混元图生视频hunyuan_video_1870170011888160769.json, 视频生成/文生视频/2025-04-05 hunyuan 5步生辰高质量视频_1908181637312749570.json, 视频生成/文生视频/ComfyOrg混元文生视频hunyuan_video_1870164228891123714.json, 视频生成/文生视频/HunyuanVideo 1.5 480P 8步LightX2V文生视频加速版V1_1992951299952099329.json, 视频生成/文生视频/HunyuanVideo 1.5 720P 20步优化版文生视频_1992813591025831937.json, 视频生成/文生视频/Image_capybara_v0_1_text_to_video_fast_2027049393966292993.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_117

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（comfyui-workflow-templates-json/hunyuan_video_text_to_video.json、图片生成/文生图/文生视频加速版_1993105222903988226.json、图片生成/文生图/混元T2V官方工作流_文生视频_1930244657111011329.json、视频生成/图生视频/8步FAST快速混元图生视频hunyuan_video_1870170011888160769.json、视频生成/文生视频/2025-04-05 hunyuan 5步生辰高质量视频_1908181637312749570.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 8/9 个有
- `VAEDecodeTiled` —— 8/9 个有
- `BasicGuider` —— 5/9 个有
- `CreateVideo` —— 5/9 个有
- `EmptyHunyuanLatentVideo` —— 5/9 个有
- `FluxGuidance` —— 5/9 个有
- `SaveVideo` —— 5/9 个有
- `CFGGuider` —— 4/9 个有
- `EmptyHunyuanVideo15Latent` —— 4/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `VHS_VideoCombine` —— 4/9 个有
- `EasyCache` —— 3/9 个有
- `JWInteger` —— 3/9 个有
- `RH_Prompter` —— 2/9 个有
- `SaveAnimatedWEBP` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
