---
name: unknown_workflow_clip_unet_vae_14
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.91325
common_nodes: [CLIPLoader, CLIPTextEncode, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Krea2｜RAW底模+Turbo 成片链_2072657816011231234.json, 图片生成/文生图/MuMu-Anima-7-1足球人妻_2072264101065216001.json, 图片生成/文生图/Wan2.2——文生图_1950509671901810689.json, 图片生成/文生图/文生图热巴_2076853328952250370.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_14

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Krea2｜RAW底模+Turbo 成片链_2072657816011231234.json、图片生成/文生图/MuMu-Anima-7-1足球人妻_2072264101065216001.json、图片生成/文生图/Wan2.2——文生图_1950509671901810689.json、图片生成/文生图/文生图热巴_2076853328952250370.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 3/4 个有
- `KSamplerAdvanced` —— 3/4 个有
- `ModelSamplingSD3` —— 2/4 个有
- `ResolutionSelector` —— 2/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `FLS_SamplerV4` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `Power Lora Loader (rgthree)` —— 1/4 个有
- `PreviewAny` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 848 - 1280 | 3 | 83% |
| 高度 | 720 | 480 - 1024 | 3 | 70% |
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 20 | 20 - 36 | 3 | 70% |
| 采样算法 | 4 | 3.5 - 8 | 3 | 61% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 848 - 1280，3 个样本，取值集中（一致性 83%）
- 高度 中位数 720，观测区间 480 - 1024，3 个样本
- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 20，观测区间 20 - 36，3 个样本
- 采样算法 中位数 4，观测区间 3.5 - 8，3 个样本
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 67%
- 风险：Prompt 约束强度(CFG) 观测到 36，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
