---
name: unknown_workflow_video_sampler_vae_33
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.956727
common_nodes: [LoadWanVideoT5TextEncoder, Primitive integer [Crystools], ShowText, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/FusionX-LORA大师级文生视频_1934653525920292866.json, 图片生成/文生图/MoviiGen+LLM电影级视频生成(kj)_1923249753776451586.json, 图片生成/文生图/Self-Forcing+LLM极速万相文生视频_1932599018294013953.json, 图片生成/文生图/WanVAC文生视频CausVid)_2059893998071930881.json, 视频生成/文生视频/FusionX-VACE大师级文生视频_1933556886325346305.json, 视频生成/文生视频/【WanVACE】3-9步极速文生视频_1923635839874551809.json, 视频生成/文生视频/仅需3-9步极速WanVACE+LLM文生视频CausVid)_1923291518734356481.json, 视频生成/文生视频/最新MoviiGen LORA+LLM电影级视频生成_1927750568260059137.json, 视频生成/文生视频/极速万相文生视频-Self-Forcing+LLM_2071395063619477505.json, 视频生成/文生视频/极速万相文生视频_2029388586482667522.json, 视频生成/文生视频/通义万相快速文生视频Self-Forcing+LLM自动视频分镜_1932781703125422081.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_33

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/FusionX-LORA大师级文生视频_1934653525920292866.json、图片生成/文生图/MoviiGen+LLM电影级视频生成(kj)_1923249753776451586.json、图片生成/文生图/Self-Forcing+LLM极速万相文生视频_1932599018294013953.json、图片生成/文生图/WanVAC文生视频CausVid)_2059893998071930881.json、视频生成/文生视频/FusionX-VACE大师级文生视频_1933556886325346305.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 11 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `Primitive integer [Crystools]`
- `ShowText`
- `Text Multiline`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 10/11 个有
- `RHHiddenNodes` —— 9/11 个有
- `WanVideoEnhanceAVideo` —— 8/11 个有
- `Text Concatenate` —— 6/11 个有
- `Fast Groups Bypasser (rgthree)` —— 5/11 个有
- `WanVideoTeaCache` —— 5/11 个有
- `easy cleanGpuUsed` —— 5/11 个有
- `ShowText|pysssss` —— 4/11 个有
- `ColorMatch` —— 3/11 个有
- `WanVideoVACEModelSelect` —— 3/11 个有
- `CM_IntToFloat` —— 2/11 个有
- `JWStringReplace` —— 2/11 个有
- `RH_LLMAPI_NODE` —— 2/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
