---
name: unknown_workflow_video_lora_sampler_43
type: Unknown Workflow
frequency: 22
level: moderate
coverage: 0.926818
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/图生视频，可编辑提示词_2058044967960010754.json, 视频生成/图生视频/1985933619749367810.json, 视频生成/图生视频/1958522667143950337.json, 视频生成/图生视频/1958523149342162945.json, 视频生成/图生视频/2053339197372674049.json, 视频生成/图生视频/2052258401169752065.json, 视频生成/图生视频/2070131687614406658.json, 视频生成/图生视频/2075910446967779329.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2083148321954291714.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2093644198363881473.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2093676510929575938.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2101617649074659330.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2101629864922140674.json, 视频生成/图生视频/wan2.2电商服装展示_模特演示视频保持一致性工作流_2105246871684993026.json, 视频生成/图生视频/2052185338583498754.json, 视频生成/图生视频/2057694453565054977.json, 视频生成/图生视频/2045576012469112833.json, 视频生成/图生视频/2056262316534091777.json, 视频生成/图生视频/2056538120484638722.json, 视频生成/图生视频/电商服装展示_模特演示视频-wan2.2_2096031121212530690.json, 视频生成/图生视频/2052610922312679426.json, 视频生成/文生视频/电商服装展示_模特演示视频-wan2.2_2051570109155688449.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_43

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/文生图/图生视频，可编辑提示词_2058044967960010754.json、视频生成/图生视频/1985933619749367810.json、视频生成/图生视频/1958522667143950337.json、视频生成/图生视频/1958523149342162945.json、视频生成/图生视频/2053339197372674049.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Int` —— 21/22 个有
- `PrimitiveInt` —— 21/22 个有
- `WanImageToVideo` —— 21/22 个有
- `INTConstant` —— 20/22 个有
- `DownloadAndLoadGIMMVFIModel` —— 19/22 个有
- `GIMMVFI_interpolate` —— 19/22 个有
- `ImageConcatMulti` —— 19/22 个有
- `PainterVRAM` —— 19/22 个有
- `SimpleMath+` —— 19/22 个有
- `ModelPatchTorchSettings` —— 3/22 个有
- `easy cleanGpuUsed` —— 3/22 个有
- `JWFloat` —— 2/22 个有
- `JWInteger` —— 2/22 个有
- `RIFE VFI` —— 2/22 个有
- `UnetLoaderGGUF` —— 2/22 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/22 个有
- `MathExpression|pysssss` —— 1/22 个有
- `WanFirstLastFrameToVideo` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 22 | 82% |
| Prompt 约束强度(CFG) | 12 | 4 - 20 | 22 | 70% |
| 采样算法 | 1 | 0 - 1 | 22 | 78% |
| 调度器 | euler | - | 22 | 100% |
| 重绘幅度 | simple | - | 22 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，22 个样本，一致性 82%
- Prompt 约束强度(CFG) 中位数 12，观测区间 4 - 20，22 个样本
- 采样算法 中位数 1，观测区间 0 - 1，22 个样本
- 调度器 最常用 euler，22 个样本，一致性 100%
- 重绘幅度 最常用 simple，22 个样本，一致性 95%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
