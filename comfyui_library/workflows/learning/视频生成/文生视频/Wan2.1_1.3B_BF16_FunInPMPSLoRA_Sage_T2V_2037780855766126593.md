---
key: 视频生成/文生视频/Wan2.1_1.3B_BF16_FunInPMPSLoRA_Sage_T2V_2037780855766126593.json
name: Wan2.1_1.3B_BF16_FunInPMPSLoRA_Sage_T2V_2037780855766126593
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1_1.3B_BF16_FunInPMPSLoRA_Sage_T2V_2037780855766126593.json
hash: aa46043e9052e858
coverage: 1
learned_at: 2026-10-11 03:48:38
nodes: [SaveVideo, CreateVideo, VAEDecode, CLIPTextEncode, KSampler, CLIPLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, VAELoader, CLIPTextEncode, EmptyHunyuanLatentVideo]
patterns: []
missing: []
parameters: {"cfg": 9, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 530666228914436, "steps": 30}
---

# 视频生成/文生视频/Wan2.1_1.3B_BF16_FunInPMPSLoRA_Sage_T2V_2037780855766126593.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.1_1.3B_BF16_FunInPMPSLoRA_Sage_T2V_2037780855766126593.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `SaveVideo`
- `CreateVideo`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`

## 关键参数

- `seed` = `530666228914436`
- `steps` = `30`
- `cfg` = `9`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`SaveVideo`、`CreateVideo`、`VAEDecode`、`CLIPTextEncode`、`KSampler`、`CLIPLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`UNETLoader`、`VAELoader`、`EmptyHunyuanLatentVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo
