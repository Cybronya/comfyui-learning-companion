---
name: unknown_workflow_video_sampler_vae_171
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [DownloadAndLoadHyVideoTextEncoder, HyVideoDecode, HyVideoModelLoader, HyVideoSampler, HyVideoTextEncode, HyVideoVAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/hunyuan-混元文生视频_1886955735341780993.json, 视频生成/文生视频/混元文生视频+LORA hunyuanvideo lora_1870173036715347969.json, 视频生成/文生视频/混元视频生成大模型-文生视频 ComfyUI-HunyuanVideoWrapper_1864642141031985153.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_171

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/hunyuan-混元文生视频_1886955735341780993.json、视频生成/文生视频/混元文生视频+LORA hunyuanvideo lora_1870173036715347969.json、视频生成/文生视频/混元视频生成大模型-文生视频 ComfyUI-HunyuanVideoWrapper_1864642141031985153.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `DownloadAndLoadHyVideoTextEncoder`
- `HyVideoDecode`
- `HyVideoModelLoader`
- `HyVideoSampler`
- `HyVideoTextEncode`
- `HyVideoVAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `HyVideoLoraSelect` —— 2/3 个有
- `RH_Prompter` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
