---
name: unknown_workflow_video_sampler_clip_75
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.8875
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyHunyuanLatentVideo, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/混元T2V官方工作流_文生视频_1930244657111011329.json, 视频生成/图生视频/8步FAST快速混元图生视频hunyuan_video_1870170011888160769.json, 视频生成/文生视频/2025-04-05 hunyuan 5步生辰高质量视频_1908181637312749570.json, 视频生成/文生视频/ComfyOrg混元文生视频hunyuan_video_1870164228891123714.json, 视频生成/文生视频/Hunyuan T2V+Lora(纳税服务)极简工作流_1903492781292032002.json, 视频生成/文生视频/Hunyuan Video + Lora_1892462560061657089.json, 视频生成/文生视频/HunyuanVideo文生视频工作流_1935331799620833282.json, 视频生成/文生视频/hunyuan_video混元视频 8G显存可用_1879187801508929537.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_75

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/混元T2V官方工作流_文生视频_1930244657111011329.json、视频生成/图生视频/8步FAST快速混元图生视频hunyuan_video_1870170011888160769.json、视频生成/文生视频/2025-04-05 hunyuan 5步生辰高质量视频_1908181637312749570.json、视频生成/文生视频/ComfyOrg混元文生视频hunyuan_video_1870164228891123714.json、视频生成/文生视频/Hunyuan T2V+Lora(纳税服务)极简工作流_1903492781292032002.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyHunyuanLatentVideo`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 7/8 个有
- `ModelSamplingSD3` —— 7/8 个有
- `VAEDecode` —— 4/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `RH_Prompter` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `ApplyFirstBlockCachePatchAdvanced` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有
- `SaveAnimatedWEBP` —— 1/8 个有
- `SaveWEBM` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
