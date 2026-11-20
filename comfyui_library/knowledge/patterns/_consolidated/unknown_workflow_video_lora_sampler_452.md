---
name: unknown_workflow_video_lora_sampler_452
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.875429
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2图生视频_2025568584335892482.json, 视频生成/图生视频/WAN2.2首尾帧_1955196269809602562.json, 视频生成/图生视频/Wan2.2  极速图生视频_2068892657300099074.json, 视频生成/图生视频/Wan2.2 14B 极速图生视频 优化版_1949991149945708545.json, 视频生成/图生视频/【图生视频】Wan2.2 14B LightX2V_1953391288357978113.json, 视频生成/图生视频/图生视频_2077340089688088578.json, 视频生成/文生视频/wan 2.2 图生视频 工作流+全节点注释_2077715652751745025.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_452

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/WAN2.2图生视频_2025568584335892482.json、视频生成/图生视频/WAN2.2首尾帧_1955196269809602562.json、视频生成/图生视频/Wan2.2  极速图生视频_2068892657300099074.json、视频生成/图生视频/Wan2.2 14B 极速图生视频 优化版_1949991149945708545.json、视频生成/图生视频/【图生视频】Wan2.2 14B LightX2V_1953391288357978113.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `WanImageToVideo` —— 6/7 个有
- `ImageResize+` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `wanBlockSwap` —— 4/7 个有
- `Int` —— 2/7 个有
- `JWInteger` —— 2/7 个有
- `SimpleMath+` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `DeepTranslatorTextNode` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有
- `WanFirstLastFrameToVideo` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | increment | - | 7 | 57% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 7 | 86% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | uni_pc | - | 7 | 57% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 increment，7 个样本，一致性 57%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，7 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 uni_pc，7 个样本，一致性 57%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
