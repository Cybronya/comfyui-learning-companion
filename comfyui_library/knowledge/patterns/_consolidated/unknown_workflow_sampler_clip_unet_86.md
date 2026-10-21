---
name: unknown_workflow_sampler_clip_unet_86
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.895429
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader]
problems: []
missing: [LoraLoader|pysssss]
members: [comfyui-workflow-templates-json/hunyuan_video_text_to_video.json, 图片生成/文生图/1909203282877624322.json, 图片生成/文生图/1930244657111011329.json, 视频生成/图生视频/1870170011888160769.json, 视频生成/文生视频/1930244657111011329.json, 视频生成/文生视频/1908181637312749570.json, 视频生成/文生视频/1870164228891123714.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_86

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（comfyui-workflow-templates-json/hunyuan_video_text_to_video.json、图片生成/文生图/1909203282877624322.json、图片生成/文生图/1930244657111011329.json、视频生成/图生视频/1870170011888160769.json、视频生成/文生视频/1930244657111011329.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyHunyuanLatentVideo` —— 6/7 个有
- `ModelSamplingSD3` —— 6/7 个有
- `VAEDecode` —— 6/7 个有
- `VAEDecodeTiled` —— 6/7 个有
- `VHS_VideoCombine` —— 5/7 个有
- `RH_Prompter` —— 2/7 个有
- `SaveAnimatedWEBP` —— 2/7 个有
- `CreateVideo` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `LoraLoader|pysssss` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `SaveVideo` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1.72 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LoraLoader|pysssss
