---
name: unknown_workflow_video_lora_sampler_812
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.933333
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, Wan22FunControlToVideo]
problems: []
missing: []
members: [平台全量/Wan2.2-native-control-fun_1955922656619057154.json, 视频生成/图生视频/【官版】Wan2.2 14B Fun Control 多模态控制_1956635710498246657.json, 视频生成/文生视频/【阡陌】 Wan2.2 Fun Control 视频控制生成_1969656393957601281.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_812

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Wan2.2-native-control-fun_1955922656619057154.json、视频生成/图生视频/【官版】Wan2.2 14B Fun Control 多模态控制_1956635710498246657.json、视频生成/文生视频/【阡陌】 Wan2.2 Fun Control 视频控制生成_1969656393957601281.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `Wan22FunControlToVideo`

**可变部分**（部分 workflow 才有）：
- `Canny` —— 2/3 个有
- `DWPreprocessor` —— 2/3 个有
- `GetVideoComponents` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `LoadVideo` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `DepthAnything_V2` —— 1/3 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `ModelPatchTorchSettings` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
