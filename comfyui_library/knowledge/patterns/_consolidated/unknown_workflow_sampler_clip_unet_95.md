---
name: unknown_workflow_sampler_clip_unet_95
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.949083
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoadImage, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader, WanImageToVideo]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2-live2D动态壁纸一键生成_2084626148595691521.json, 图片生成/图生图/wan2.2+lightx2v-8步图生视频-ComfyUI官方_1949980973129752578.json, 视频生成/图生视频/Wan2.2 14B I2V 图生视频工作流示例_1950475750447173633.json, 视频生成/图生视频/wan2.2+Sage加速图生视频-ComfyUI官方_1949982981533384705.json, 视频生成/图生视频/wan2.2+lightx2v-4步图生视频-ComfyUI官方_1949988822005235714.json, 视频生成/图生视频/wan2.2+lightx2v-4步图生视频-ComfyUI官方_1950054777926369282.json, 视频生成/图生视频/wan2.2+lightx2v-8步图生视频-ComfyUI官方（极速）_1950460812701949953.json, 视频生成/图生视频/wan2.2+lightx2v加速图生视频_1950007304294981633.json, 视频生成/图生视频/wan2.2+lightx2v加速图生视频_1954724255986544642.json, 视频生成/图生视频/wan2.2图生视频-ComfyUI官方_1949851914386194434.json, 视频生成/图生视频/wan2.2图生视频-ComfyUI官方_1950015498596564993.json, 视频生成/图生视频/【阡陌】SageAttention+wan2.2+light4步加速lora提速40%图生视频工作流_1968502067780300801.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_95

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Wan2.2-live2D动态壁纸一键生成_2084626148595691521.json、图片生成/图生图/wan2.2+lightx2v-8步图生视频-ComfyUI官方_1949980973129752578.json、视频生成/图生视频/Wan2.2 14B I2V 图生视频工作流示例_1950475750447173633.json、视频生成/图生视频/wan2.2+Sage加速图生视频-ComfyUI官方_1949982981533384705.json、视频生成/图生视频/wan2.2+lightx2v-4步图生视频-ComfyUI官方_1949988822005235714.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 9/12 个有
- `LoraLoaderModelOnly` —— 9/12 个有
- `MathExpression|pysssss` —— 9/12 个有
- `PathchSageAttentionKJ` —— 9/12 个有
- `Primitive integer [Crystools]` —— 9/12 个有
- `Text Multiline` —— 9/12 个有
- `CFGZeroStar` —— 1/12 个有
- `LayerUtility: PurgeVRAM V2` —— 1/12 个有
- `ModelPatchTorchSettings` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 12 | 75% |
| Prompt 约束强度(CFG) | 8 | 4 - 20 | 12 | 37% |
| 采样算法 | 1 | 1 - 3.5 | 12 | 40% |
| 调度器 | euler | - | 12 | 50% |
| 重绘幅度 | simple | - | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，12 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 20，12 个样本，取值分散，一致性仅 37%
- 采样算法 中位数 1，观测区间 1 - 3.5，12 个样本，取值分散，一致性仅 40%
- 调度器 最常用 euler，12 个样本，一致性 50%
- 重绘幅度 最常用 simple，12 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
