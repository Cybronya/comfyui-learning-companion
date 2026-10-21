---
name: unknown_workflow_video_lora_sampler_374
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.9655
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2018039225307893762.json, 视频生成/图生视频/1979808803409530882.json, 视频生成/文生视频/Wan2.2T2V文生视频_1983620285146537985.json, 视频生成/文生视频/Wan2.2多版本模型对比工作流（T2V文生视频）_1979813231558561793.json, 视频生成/文生视频/Wan2.2建筑生长文生视频_1989132418231701506.json, 视频生成/文生视频/加强版Wan2.2--T2V生长建筑文生视频_1980564390359552001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_374

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2018039225307893762.json、视频生成/图生视频/1979808803409530882.json、视频生成/文生视频/Wan2.2T2V文生视频_1983620285146537985.json、视频生成/文生视频/Wan2.2多版本模型对比工作流（T2V文生视频）_1979813231558561793.json、视频生成/文生视频/Wan2.2建筑生长文生视频_1989132418231701506.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 5/6 个有
- `GIMMVFI_interpolate` —— 5/6 个有
- `LayerUtility: PurgeVRAM V2` —— 5/6 个有
- `PrimitiveInt` —— 5/6 个有
- `EmptyHunyuanLatentVideo` —— 4/6 个有
- `LoadImage` —— 2/6 个有
- `Text Concatenate` —— 2/6 个有
- `WanImageToVideo` —— 2/6 个有
- `ImageFromBatch+` —— 1/6 个有
- `ResizeLongestToNode` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `ttN seed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 50% |
| Prompt 约束强度(CFG) | 8 | 6 - 12 | 6 | 78% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler | - | 6 | 83% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 12，6 个样本
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 83%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
