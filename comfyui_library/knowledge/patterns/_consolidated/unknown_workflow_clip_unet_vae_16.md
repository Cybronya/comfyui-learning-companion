---
name: unknown_workflow_clip_unet_vae_16
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.921
common_nodes: [CLIPLoader, CLIPTextEncode, PreviewImage, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Krea2｜RAW底模+Turbo 成片链_2072657816011231234.json, 图片生成/文生图/MuMu-Anima-7-1足球人妻_2072264101065216001.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_16

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Krea2｜RAW底模+Turbo 成片链_2072657816011231234.json、图片生成/文生图/MuMu-Anima-7-1足球人妻_2072264101065216001.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `PreviewImage`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `FLS_SamplerV4` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `Power Lora Loader (rgthree)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |
| 采样步数 | randomize | - | 1 | 100% |
| Prompt 约束强度(CFG) | 36 | - | 1 | 100% |
| 采样算法 | 4 | - | 1 | 100% |
| 调度器 | euler | - | 1 | 100% |
| 重绘幅度 | simple | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 风险：Prompt 约束强度(CFG) 观测到 36，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
