---
name: unknown_workflow_video_sampler_vae_79
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.989857
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/5秒治愈短视频生成-Wan2.1_1895790178705473538.json, 视频生成/文生视频/AccVid加速Wan-T2V文生视频_1927915549706338305.json, 视频生成/文生视频/CineScale-wan2.1-至高2k文生视频测试_1959895753969840129.json, 视频生成/文生视频/EchoShot 1.3B单主体多镜头一致性文生视频_1949888424809553922.json, 视频生成/文生视频/EchoShot-跨镜头一致性_1949779565657899010.json, 视频生成/文生视频/wan-AccVideo-T2V文生视频_1927926350613463041.json, 视频生成/文生视频/仅需3-9步极速文生视频WanVACE+CausVid_1924372992019918849.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_79

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/5秒治愈短视频生成-Wan2.1_1895790178705473538.json、视频生成/文生视频/AccVid加速Wan-T2V文生视频_1927915549706338305.json、视频生成/文生视频/CineScale-wan2.1-至高2k文生视频测试_1959895753969840129.json、视频生成/文生视频/EchoShot 1.3B单主体多镜头一致性文生视频_1949888424809553922.json、视频生成/文生视频/EchoShot-跨镜头一致性_1949779565657899010.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 7 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoBlockSwap` —— 5/7 个有
- `WanVideoLoraSelect` —— 5/7 个有
- `DF_Integer` —— 3/7 个有
- `String Literal` —— 3/7 个有
- `WanVideoEnhanceAVideo` —— 3/7 个有
- `WanVideoTorchCompileSettings` —— 2/7 个有
- `WanVideoVACEModelSelect` —— 2/7 个有
- `DeepTranslatorTextNode` —— 1/7 个有
- `Note _O` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `WanVideoSetRadialAttention` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
