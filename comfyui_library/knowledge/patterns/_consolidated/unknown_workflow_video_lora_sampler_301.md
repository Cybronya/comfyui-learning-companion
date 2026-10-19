---
name: unknown_workflow_video_lora_sampler_301
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.975
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2000837178416656386.json, 视频生成/图生视频/2000842508747800577.json, 视频生成/图生视频/1968955228710133762.json, 视频生成/图生视频/1989350434903085058.json, 视频生成/图生视频/1950026797163438082.json, 视频生成/图生视频/1952642819863318529.json, 视频生成/图生视频/1953391288357978113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_301

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2000837178416656386.json、视频生成/图生视频/2000842508747800577.json、视频生成/图生视频/1968955228710133762.json、视频生成/图生视频/1989350434903085058.json、视频生成/图生视频/1950026797163438082.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 4/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `WanImageToVideo` —— 4/7 个有
- `LayerUtility: PurgeVRAM` —— 3/7 个有
- `RH_LLMAPI_NODE` —— 3/7 个有
- `ShowText|pysssss` —— 3/7 个有
- `WanFirstLastFrameToVideo` —— 3/7 个有
- `SaveImage` —— 2/7 个有
- `easy imageConcat` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `PreviewImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 100% |
| Prompt 约束强度(CFG) | 6 | 4 - 8 | 7 | 74% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 57% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 8，7 个样本
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 57%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
