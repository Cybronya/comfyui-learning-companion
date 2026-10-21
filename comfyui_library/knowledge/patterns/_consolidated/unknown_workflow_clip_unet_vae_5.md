---
name: unknown_workflow_clip_unet_vae_5
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.929222
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1978720948956319746.json, 视频生成/文生视频/1分钟生成一条视频，Wan2.2-Lightx2v，新版加速LoRA又更新！_1987367248606244865.json, 视频生成/文生视频/UnifiedReward-Flex LoRA实测：Wan2.2动作逻辑与物理表现提升_2029085278756937729.json, 视频生成/文生视频/UnifiedReward-Flex LoRA：Wan2.2动作逻辑与物理表现升级_2029392351566766081.json, 视频生成/文生视频/1950466013982842881.json, 视频生成/文生视频/Wan2.2_文生视频4步LoRA加速-B站UP主@好奇漫步_1983147396660129793.json, 视频生成/文生视频/1967793949974867969.json, 视频生成/文生视频/1967560743048581122.json, 视频生成/文生视频/1954115283415920642.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_5

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1978720948956319746.json、视频生成/文生视频/1分钟生成一条视频，Wan2.2-Lightx2v，新版加速LoRA又更新！_1987367248606244865.json、视频生成/文生视频/UnifiedReward-Flex LoRA实测：Wan2.2动作逻辑与物理表现提升_2029085278756937729.json、视频生成/文生视频/UnifiedReward-Flex LoRA：Wan2.2动作逻辑与物理表现升级_2029392351566766081.json、视频生成/文生视频/1950466013982842881.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 8/9 个有
- `EmptyHunyuanLatentVideo` —— 7/9 个有
- `LoraLoaderModelOnly` —— 7/9 个有
- `LoadImage` —— 5/9 个有
- `Label (rgthree)` —— 4/9 个有
- `WanImageToVideo` —— 2/9 个有
- `FSamplerAdvanced` —— 1/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `UnetLoaderGGUF` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 50% |
| Prompt 约束强度(CFG) | 7 | 4 - 20 | 8 | 38% |
| 采样算法 | 1 | 1 - 3.5 | 8 | 39% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 7，观测区间 4 - 20，8 个样本，取值分散，一致性仅 38%
- 采样算法 中位数 1，观测区间 1 - 3.5，8 个样本，取值分散，一致性仅 39%
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
