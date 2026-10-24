---
name: unknown_workflow_upscale_latent_upscale_sampler_10
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.941125
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, DualCLIPLoader, HunyuanVideo15LatentUpscaleWithModel, HunyuanVideo15SuperResolution, KSamplerSelect, LatentUpscaleModelLoader, ModelSamplingSD3, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/HUNYUAN 1.5 I2V SR_2073280696038289410.json, 视频生成/图生视频/HUNYUAN+1.5+I2V+8Step_2074119499955130370.json, 视频生成/图生视频/workflow_2073289414930944001.json, 视频生成/图生视频/混元1.5I2V+超分-Aiwood_1992198526646153217.json, 视频生成/图生视频/混元1.5_图生视频_场景推进画面首选_1997913784465391617.json, 视频生成/文生视频/HunyuanVideo_1.5加速图生视频1080p_1993246112486195202.json, 视频生成/文生视频/HunyuanVideo_1.5加速图生视频1080p（熊叔版）_1993572660164706305.json, 视频生成/文生视频/HunyuanVideo_1.5加速文生视频1080p_1993277000070660097.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_10

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/HUNYUAN 1.5 I2V SR_2073280696038289410.json、视频生成/图生视频/HUNYUAN+1.5+I2V+8Step_2074119499955130370.json、视频生成/图生视频/workflow_2073289414930944001.json、视频生成/图生视频/混元1.5I2V+超分-Aiwood_1992198526646153217.json、视频生成/图生视频/混元1.5_图生视频_场景推进画面首选_1997913784465391617.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `HunyuanVideo15LatentUpscaleWithModel`
- `HunyuanVideo15SuperResolution`
- `KSamplerSelect`
- `LatentUpscaleModelLoader`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 7/8 个有
- `CLIPVisionLoader` —— 7/8 个有
- `HunyuanVideo15ImageToVideo` —— 7/8 个有
- `LoadImage` —— 7/8 个有
- `VAEDecode` —— 6/8 个有
- `VAEDecodeTiled` —— 5/8 个有
- `VHS_VideoCombine` —— 5/8 个有
- `CreateVideo` —— 3/8 个有
- `DisableNoise` —— 3/8 个有
- `GetImageSize` —— 3/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `SaveVideo` —— 3/8 个有
- `SplitSigmas` —— 3/8 个有
- `easy cleanGpuUsed` —— 3/8 个有
- `ResizeLongestToNode` —— 2/8 个有
- `EmptyHunyuanVideo15Latent` —— 1/8 个有
- `ResizeImagesByLongerEdge` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
