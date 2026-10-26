---
name: unknown_workflow_video_lora_sampler_350
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.914
common_nodes: [CLIPLoader, CLIPTextEncode, Int, KSamplerAdvanced, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, Power Lora Loader (rgthree), RIFE VFI, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/0828首尾帧+Wan2.2-I2V+4步加速工作流8_1962165957621911554.json, 视频生成/图生视频/wan2.2首中尾帧人物一致自用流程_2046793067730051073.json, 视频生成/图生视频/自用首尾帧_Wan2.2_Lightx版_2046526695909363713.json, 视频生成/图生视频/首尾帧 Wan2.2-I2V 4步加速Lora首尾帧【Q8量化版】_1956638598607900673.json, "视频生成/文生视频/WAN 2.2 -14B 首帧+尾帧, LIGHTX2V + 视频补帧_1952395294703071233.json", 视频生成/文生视频/Wan2.2-I2V + Lightx_2V 【新版2.2-4步加速Lora】图生视频结构清晰版_1954923648895389698.json, 视频生成/文生视频/首尾帧 Wan2.2-I2V + Lightx_2V 【新版2.2-4步加速Lora】图生视频流程_1956007540079427585.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_350

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/0828首尾帧+Wan2.2-I2V+4步加速工作流8_1962165957621911554.json、视频生成/图生视频/wan2.2首中尾帧人物一致自用流程_2046793067730051073.json、视频生成/图生视频/自用首尾帧_Wan2.2_Lightx版_2046526695909363713.json、视频生成/图生视频/首尾帧 Wan2.2-I2V 4步加速Lora首尾帧【Q8量化版】_1956638598607900673.json、视频生成/文生视频/WAN 2.2 -14B 首帧+尾帧, LIGHTX2V + 视频补帧_1952395294703071233.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Int`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Power Lora Loader (rgthree)`
- `RIFE VFI`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `WanVideoNAG` —— 6/7 个有
- `ImageScale` —— 5/7 个有
- `SaveImage` —— 5/7 个有
- `WanFirstLastFrameToVideo` —— 5/7 个有
- `CreateVideo` —— 2/7 个有
- `INTConstant` —— 2/7 个有
- `PreViewVideo` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `CLIPVisionEncode` —— 1/7 个有
- `CLIPVisionLoader` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `WanFirstMiddleLastFrameToVideo` —— 1/7 个有
- `WanImageToVideo` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 100% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 7 | 91% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，7 个样本，取值集中（一致性 91%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
