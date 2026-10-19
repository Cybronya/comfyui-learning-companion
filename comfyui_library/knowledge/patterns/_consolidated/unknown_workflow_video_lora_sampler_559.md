---
name: unknown_workflow_video_lora_sampler_559
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8745
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/Qwen3-VL反推视频提示词WAN22生成视频_1988333023324233729.json, 视频生成/文生视频/Qwen3VL_视频分镜反推提示词_文生视频_Comfyui官方流_1983729190623223809.json, 视频生成/文生视频/Wan2.2文生视频-高质量_1994736642340556801.json, 视频生成/文生视频/wan2_2_t2v_Qwen3VL 参考视频识别 + 文生视频流程_1981031658872770562.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_559

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/Qwen3-VL反推视频提示词WAN22生成视频_1988333023324233729.json、视频生成/文生视频/Qwen3VL_视频分镜反推提示词_文生视频_Comfyui官方流_1983729190623223809.json、视频生成/文生视频/Wan2.2文生视频-高质量_1994736642340556801.json、视频生成/文生视频/wan2_2_t2v_Qwen3VL 参考视频识别 + 文生视频流程_1981031658872770562.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL_Advanced` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `easy clearCacheAll` —— 2/4 个有
- `ModelPatchTorchSettings` —— 1/4 个有
- `VHS_VideoInfoLoaded` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 75% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 4 | 81% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，4 个样本，取值集中（一致性 81%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
