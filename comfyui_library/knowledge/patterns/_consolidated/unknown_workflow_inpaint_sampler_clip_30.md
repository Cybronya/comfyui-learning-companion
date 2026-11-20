---
name: unknown_workflow_inpaint_sampler_clip_30
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.901571
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncodeForInpaint]
problems: []
missing: []
members: [图片生成/图生图/「背景延展 _ Outpainting」_2110961289022492673.json, 图片生成/图生图/扩图_2057399705939832833.json, 平台全量/ComfyUI-图像修复_1934887506850848770.json, 平台全量/ComfyUI-扩展图片_1934898657344823297.json, 平台全量/ComfyUI官方示例3：inpaint工作流详解_1931356892193292290.json, 平台全量/ComfyUI官方示例4：Outpainting工作流详解 _ ComfyUI从入门到精通_1931598672390193154.json, 平台全量/建筑局部重绘_2061150700373102594.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_30

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/「背景延展 _ Outpainting」_2110961289022492673.json、图片生成/图生图/扩图_2057399705939832833.json、平台全量/ComfyUI-图像修复_1934887506850848770.json、平台全量/ComfyUI-扩展图片_1934898657344823297.json、平台全量/ComfyUI官方示例3：inpaint工作流详解_1931356892193292290.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncodeForInpaint`

**可变部分**（部分 workflow 才有）：
- `ImagePadForOutpaint` —— 4/7 个有
- `PreviewImage` —— 2/7 个有
- `ImageCompositeMasked` —— 1/7 个有
- `MaskToImage` —— 1/7 个有
- `preview_mask` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 7 | 84% |
| Prompt 约束强度(CFG) | 7 | 5.5 - 8 | 7 | 88% |
| 采样算法 | dpmpp_2m | - | 7 | 43% |
| 调度器 | karras | - | 7 | 71% |
| 重绘幅度 | 1 | 0.85 - 1 | 7 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，7 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 5.5 - 8，7 个样本，取值集中（一致性 88%）
- 采样算法 最常用 dpmpp_2m，7 个样本，一致性 43%
- 调度器 最常用 karras，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 0.85 - 1，7 个样本，取值集中（一致性 95%）
