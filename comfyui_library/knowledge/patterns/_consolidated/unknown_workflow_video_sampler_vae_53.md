---
name: unknown_workflow_video_sampler_vae_53
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.967667
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: [String Literal]
members: [视频生成/文生视频/1949779565657899010.json, 视频生成/文生视频/1959895753969840129.json, 视频生成/文生视频/1895790178705473538.json, 视频生成/文生视频/1927915549706338305.json, 视频生成/文生视频/CineScale-wan2.1-至高2k文生视频测试_2072999630763499520.json, 视频生成/文生视频/1949888424809553922.json, 视频生成/文生视频/EchoShot-跨镜头一致性_2072999661792960512.json, 视频生成/文生视频/1927926350613463041.json, 视频生成/文生视频/1924372992019918849.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_53

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/1949779565657899010.json、视频生成/文生视频/1959895753969840129.json、视频生成/文生视频/1895790178705473538.json、视频生成/文生视频/1927915549706338305.json、视频生成/文生视频/CineScale-wan2.1-至高2k文生视频测试_2072999630763499520.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 9 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 7/9 个有
- `WanVideoBlockSwap` —— 6/9 个有
- `String Literal` —— 5/9 个有
- `WanVideoEnhanceAVideo` —— 4/9 个有
- `DF_Integer` —— 3/9 个有
- `WanVideoSetRadialAttention` —— 2/9 个有
- `WanVideoTorchCompileSettings` —— 2/9 个有
- `WanVideoVACEModelSelect` —— 2/9 个有
- `DeepTranslatorTextNode` —— 1/9 个有
- `Note _O` —— 1/9 个有
- `SimpleMath+` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：String Literal
