---
name: unknown_workflow_controlnet_upscale
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9165
common_nodes: [ControlNetApply, ControlNetLoader, Efficient Loader, LoadImage, SaveImage, UltimateSDUpscale, UpscaleModelLoader]
problems: []
missing: []
members: [图片生成/图生图/一键高清放大2倍-1.5_1921233721729679361.json, 平台全量/Nice QR Code_1892782344322125826.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键高清放大2倍-1.5_1921233721729679361.json、平台全量/Nice QR Code_1892782344322125826.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `ControlNetApply`
- `ControlNetLoader`
- `Efficient Loader`
- `LoadImage`
- `SaveImage`
- `UltimateSDUpscale`
- `UpscaleModelLoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/2 个有
- `KSampler (Efficient)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1.2 | - | 2 | 83% |
| 采样步数 | 50 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 6 | - | 1 | 100% |
| 采样算法 | dpmpp_2m | - | 1 | 100% |
| 调度器 | karras | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1.2，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
