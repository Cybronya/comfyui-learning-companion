---
name: unknown_workflow_inpaint_sampler_clip_45
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9308
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, NunchakuFluxDiTLoader, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/nunchaku-Flux-Fill手部加速修复_1909953672649080833.json, 图片生成/图生图/nunchaku去边角水印_1929685738722377729.json, 图片生成/图生图/极速万物清除，双节棍Nunchaku 加速版万物消除_1929489211492089857.json, 图片生成/图生图/极速去水印_换衣_加水印  Nunchaku+FluxFill局部重绘_1917237782241284098.json, 平台全量/极速版万物消除SOTA_1929758101149270018.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_45

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/nunchaku-Flux-Fill手部加速修复_1909953672649080833.json、图片生成/图生图/nunchaku去边角水印_1929685738722377729.json、图片生成/图生图/极速万物清除，双节棍Nunchaku 加速版万物消除_1929489211492089857.json、图片生成/图生图/极速去水印_换衣_加水印  Nunchaku+FluxFill局部重绘_1917237782241284098.json、平台全量/极速版万物消除SOTA_1929758101149270018.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `NunchakuFluxLoraLoader` —— 4/5 个有
- `JWInteger` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `Bjornulf_FreeVRAM` —— 1/5 个有
- `CR Prompt Text` —— 1/5 个有
- `ImageAndMaskResizeNode` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 5 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，5 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
